from datetime import datetime, timedelta
from .models import DriverFees,VehicalFees,ParkingFees
from django.contrib.auth.models import Group
from .ParkingException import ParkingLotFullException
"""
Method to calculate charge of parking based on types

Keyword arguments:
vehcile_details -- data dictionary of vehicle details
Return: it return total parking charge of vehicle 
"""

def calculate_charges(vehicle_details):
    cost_for_vhecle_type = VehicalFees.objects.get(vehicle_type=vehicle_details.vehicle_type)
    hours =  get_parking_hours(vehicle_details.entry_time, vehicle_details.exit_time)
    total_charges = 0
    username = vehicle_details.user_details
    group = Group.objects.get(user=username)
    driver_type_charges = DriverFees.objects.get(driver_type=group)
    if driver_type_charges.cost != 0 :
        time_charges = round((hours * cost_for_vhecle_type.cost),3)
        parking_type_charges = ParkingFees.objects.get(parking_type=vehicle_details.parking_type)
        total_charges = parking_type_charges.cost+driver_type_charges.cost+time_charges
    return total_charges
    
"""
Get parking hours

Keyword arguments:
entry_time,exit_time -- vehicle entry time and unparked time of vehicle
Return: it return the time in hours
"""

def get_parking_hours(entry_time, exit_time):
    total_time = exit_time - entry_time
    return total_time.seconds/3600

"""
Get slot from the parking slot

Keyword arguments:
slot_list -- slots of already parked vehicles
Return: returns the slot based on the order of slot number
"""

def get_slot(slot_list):
    slots_400 = list(range(0,400))
    rest_slots = set(slots_400).difference(set(slot_list))
    try:
        vehicle_slot = list(rest_slots)[0]
        return vehicle_slot
    except IndexError as e:
        raise ParkingLotFullException()
    
