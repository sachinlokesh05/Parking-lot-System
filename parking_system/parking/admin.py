from django.contrib import admin
from .models import Log,Parking,DriverFees,ParkingFees,VehicalFees
# Register your models here.


class ParkingAdmin(admin.ModelAdmin):
    model = Parking
    fileds = "__all__"
admin.site.register(Parking,ParkingAdmin)


class VehicleAdmin(admin.ModelAdmin):
    model = VehicalFees
    fileds = "__all__"
admin.site.register(VehicalFees,VehicleAdmin)

class ParkingtypeAdmin(admin.ModelAdmin):
    model = ParkingFees
    fileds = "__all__"
admin.site.register(ParkingFees,ParkingtypeAdmin)

class DriverAdmin(admin.ModelAdmin):
    model = DriverFees
    fileds = "__all__"
admin.site.register(DriverFees,DriverAdmin)