from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from parking.models import Parking
from .serializers import CreateParkingSerializer
# Create your views here.

class CreateParkingView(ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer

