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
from .utils import calculate_cost
from django.core.exceptions import ObjectDoesNotExist
class CreateParkingView(LoginRequiredMixin,ListCreateAPIView):
    login_url= "login"
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer


@login_required(login_url="login")
@api_view(['GET','POST'])
def Unparking(request,*args,**kwargs):
    data = request.query_params
    unparking_vehicle = UnparkingSerializer(data=data,partial=True)
    unparking_vehicle.is_valid(raise_exception=True)
    try:
        parking_obj = Parking.objects.filter(vehicle_number=request.query_params['vehicle_number'],exit_time=None).latest('id')
    except ObjectDoesNotExist:
        return Response(data="Vehicle is already unparked,Sorry",status=status.HTTP_400_BAD_REQUEST)
    value = unparking_vehicle.update(instance=parking_obj,validated_data=unparking_vehicle.data)
    return Response(data="Unparking succefully,Thank You",status=status.HTTP_200_OK)
