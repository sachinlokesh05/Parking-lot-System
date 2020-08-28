from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from parking.models import Parking
from .serializers import CreateParkingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import UnparkingSerializer
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .utils import calculate_charges
class CreateParkingView(LoginRequiredMixin,ListCreateAPIView):
    login_url= "login"
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer

""""
Unparking API

Keyword arguments:
request,vehicle_number -- request parameter and vehicle number
Return: unpark the vehicle and return the parking charges
"""

@login_required(login_url="login")
@api_view(['GET'])
def Unparking(request,*args,**kwargs):
    data = request.query_params
    unparking_vehicle = UnparkingSerializer(data=data,partial=True)
    unparking_vehicle.is_valid(raise_exception=True)
    try:
        parking_obj = Parking.objects.filter(vehicle_number=request.query_params['vehicle_number'],exit_time=None).latest('id')
    except ObjectDoesNotExist:
        return Response(data="Vehicle is already unparked,Sorry",status=status.HTTP_400_BAD_REQUEST)
    value = unparking_vehicle.update(instance=parking_obj,validated_data=unparking_vehicle.data)
    vehicle_details=value.only('id','vehicle_type','entry_time','exit_time','user_details','parking_type')
    print(vehicle_details[0])
    total_charges = calculate_charges(vehicle_details[0])
    return Response(data=f"Unparking succefully,Thank You,Your Parking Charge is: {total_charges}",status=status.HTTP_200_OK)
