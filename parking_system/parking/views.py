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
# Create your views here.

class CreateParkingView(LoginRequiredMixin,ListCreateAPIView):
    login_url= "login"
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer


@login_required(login_url="login")
@api_view(['GET'])
def Unparking(request,*args,**kwargs):
    unparking_vehicle = UnparkingSerializer(data=request.GET)
    unparking_vehicle.is_valid(raise_exception=True)
    return Response(data="Unparking succefully,Thank You",status=status.HTTP_200_OK)