from rest_framework.exceptions import APIException
from rest_framework import status
class VehicleDoesNotExist(APIException):
    pass

class ParkingLotFullException(APIException):
    default_detail = "Parking Lot is Full,Sorry for the interruption"
    status_code = status.HTTP_406_NOT_ACCEPTABLE