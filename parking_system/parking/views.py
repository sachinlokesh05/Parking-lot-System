from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from parking.models import Parking
from .serializers import CreateParkingSerializer,DriverParkingSerializer,PolicemanParkingSerializer,OwnerParkingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import UnparkingSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class CreateParkingView(ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = CreateParkingSerializer


@login_required(login_url="login")
@api_view(['GET'])
def Unparking(request,*args,**kwargs):
    unparking_vehicle = UnparkingSerializer(data=request.GET)
    unparking_vehicle.is_valid(raise_exception=True)
    return Response(data="Unparking succefully,Thank You",status=status.HTTP_200_OK)



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

   