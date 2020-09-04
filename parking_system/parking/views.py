from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from parking.models import Parking
from .serializers import CreateParkingSerializer,DriverParkingSerializer,PolicemanParkingSerializer,OwnerParkingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import UnparkingSerializer
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .utils import calculate_charges
from rest_framework import viewsets
from django.db import DataError
from parking.mailservice import EmailClass
from smtplib import SMTPException
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
    if not data: 
        return Response(data="Please mention valid vehicle number",status=status.HTTP_400_BAD_REQUEST) 
    unparking_vehicle = UnparkingSerializer(data=data,partial=True)
    unparking_vehicle.is_valid(raise_exception=True)
    try:
        parking_obj = Parking.objects.filter(vehicle_number=request.query_params['vehicle_number'],exit_time=None).latest('id')
        value = unparking_vehicle.update(instance=parking_obj,validated_data=unparking_vehicle.data)
        vehicle_details=value.only('id','vehicle_type','entry_time','exit_time','user_details','parking_type')
        total_charges = calculate_charges(vehicle_details[0])
        kwargs['charges'] = total_charges
        kwargs['vehicle_owner'] = request.user.username
        kwargs['vehicle_number'] = vehicle_details[0].vehicle_number
        kwargs['subject'] = "Parking Alert !!!!!"
        kwargs['recepients'] = vehicle_details[0].user_details.email
        kwargs['template_name'] = "emails/customer_unparking_alert.html"
        EmailClass.send_email(**kwargs)
        return Response(data=f"Unparking succefully,Thank You,Your Parking Charge is: {total_charges}",status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(data="Vehicle is already unparked,Sorry",status=status.HTTP_400_BAD_REQUEST)
    except DataError as e :
        return Response(data=f"Something happend with Data base {e} ",status=status.HTTP_400_BAD_REQUEST)
    except SMTPException as e :
        return ('There was an error sending an email: ', e)


class GetVehicle(viewsets.ReadOnlyModelViewSet):
    serializer_class = CreateParkingSerializer
    driver_serialiser_class = DriverParkingSerializer
    owner_serialiser_class = OwnerParkingSerializer
    policeman_serialiser_class = PolicemanParkingSerializer
    queryset = Parking.objects.all()

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        role = self.request.user.groups
        # roles = [
        #     'driver',
        #     "owner",
        #     "poloceman"
        # ].__getattribute__()
        print(role)
        if self.request.user.groups.filter(name='driver').exists():
            return self.driver_serialiser_class
        if self.request.user.groups.filter(name='owner').exists():
            return self.owner_serialiser_class
        if self.request.user.groups.filter(name='policeman').exists():
            return self.policeman_serialiser_class
                
        return super().get_serializer_class()

