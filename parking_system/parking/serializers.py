from rest_framework import serializers
from .models import Parking,Log
from mongoengine.errors import DoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models import Count, F, Subquery, Value
from .ParkingException import VehicleDoesNotExist
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class CreateParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"

        exclude = ['entry_time','exit_time',"slot","user_details"]

    def create(self, validated_data):
        from random import randint
        query_slot = 1
        new_slot = 0
        while  query_slot :
            new_slot = randint(0,400)
            try:
                query_slot = Parking.objects.get(slot=new_slot)
            except ObjectDoesNotExist:
                query_slot = 0
        validated_data["slot"] = new_slot
        return super().create(validated_data)

    def save(self, **kwargs):
        self.validated_data['user_details'] = self._context['request'].user 
        user = self.validated_data['user_details']
        try:
            email_list = User.objects.get(username=user).email
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
        except ObjectDoesNotExist as e:
            print(e)
            raise VehicleDoesNotExist(detail="Vehicle is not present with the Vehicle Number",code=400)
        return super(UnparkingSerializer, self).validate(data)

    def update(self, instance, validated_data):
        validated_data['slot']=None
        validated_data['exit_time']=timezone.now()
        parking_obj = Parking.objects.filter(vehicle_number=validated_data['vehicle_number']).order_by("-pk")[:1]
        obj = super().update(instance, validated_data)
        return parking_obj