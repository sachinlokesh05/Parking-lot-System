from django.contrib import admin
from .models import Log,Parking
# Register your models here.


class ParkingAdmin(admin.ModelAdmin):
    model = Parking
    fileds = "__all__"



admin.site.register(Parking,ParkingAdmin)
