from rest_framework import serializers
from .models import Parking,Log
from mongoengine.errors import DoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.models import User

class CreateParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # fields = "__all__"

        exclude = ['entry_time','exit_time',"slot"]

    def create(self, validated_data):
        from random import randint
        query_slot = 1
        new_slot = 0
        while  query_slot :
            new_slot = randint(0,400)
            try:
                query_slot = Parking.objects.get(slot=new_slot)
            except Exception:
                query_slot = 0
        validated_data["slot"] = new_slot

        return super().create(validated_data)

    def save(self, **kwargs):
        user = self.validated_data['user_details']
        try:
            email_list = User.objects.get(username=user).email
        except Exception:
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