from rest_framework import serializers
from .models import Parking,Log
from mongoengine.errors import DoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models import Count, F, Subquery, Value
from .ParkingException import VehicleDoesNotExist,ParkingLotFullException
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .mailservice import EmailClass
from parking_system.settings import EMAIL_HOST_USER
import datetime
from smtplib import SMTPException
from .utils import get_slot
import random
class CreateParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"

        exclude = ['entry_time','exit_time',"slot","user_details"]

    def create(self, validated_data,**kwargs):
        try:
            query_slot = Parking.objects.values_list('slot', flat=True)
            slot_list = list(query_slot)
            new_slot = get_slot(slot_list)
            validated_data["slot"] = new_slot
            kwargs['subject'] = "Parking Alert !!!!!"
            kwargs['vehicle_owner'] = validated_data['user_details'].username
            kwargs['vehicle_number'] = validated_data['vehicle_number']
            kwargs['vehicle_slot'] = validated_data['slot']
            kwargs['start_time'] = datetime.datetime.now()
            kwargs['recepients'] = validated_data['user_details'].email
            kwargs['template_name'] = "emails/customer_parking_alert.html"
            EmailClass.send_email(**kwargs)
            return super().create(validated_data)
        except SMTPException as e :
            return ('There was an error sending an email: ', e)
        except ParkingLotFullException as e :
            raise ParkingLotFullException()
        

    def save(self, **kwargs):
        self.validated_data['user_details'] = self._context['request'].user 
        user = self.validated_data['user_details']
        try:
            email_list = User.objects.get(username=user)
        except ObjectDoesNotExist:
            raise DoesNotExist("User email Not Exist")
        return super().save(**kwargs)

class OwnerParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"


        exclude = ['entry_time','exit_time']

class DriverParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"

        exclude = ['entry_time','exit_time',"user_details","slot","vehicle_number"]


class PolicemanParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"

        exclude = ['entry_time','exit_time']


class UnparkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields= ['vehicle_number']

    def validate(self,data):
        vehicle_number = data.get('vehicle_number')
        try:
            vehicle_details = Parking.objects.filter(vehicle_number=vehicle_number)
            return super(UnparkingSerializer, self).validate(data)
        except ObjectDoesNotExist as e:
            raise VehicleDoesNotExist(detail="Vehicle is not present with the Vehicle Number",code=400)
        

    def update(self, instance, validated_data):
        validated_data['slot']=None
        validated_data['exit_time']=timezone.now()
        parking_obj = Parking.objects.filter(vehicle_number=validated_data['vehicle_number']).order_by("-pk")[:1]
        obj = super().update(instance, validated_data)
        return parking_obj