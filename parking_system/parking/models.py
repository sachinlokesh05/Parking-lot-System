from djongo import models
from django.contrib.auth.models import User
import mongoengine
class Log(models.Model):
    """Model definition for Log."""

    
    class Meta:
        """Meta definition for Log."""
        abstract = True

    def __str__(self):
        """Unicode representation of Log."""
        return str(self.entry_time)+" to "+str(self.exit_time)


 
class Parking(models.Model):
    """Model definition for Parking."""
    user_details = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20,blank = False)
    vehicle_color = models.CharField(max_length=100,blank = False)
    vehicles = (
        ('Bike','Bike'),
        ('Car','Car'),
        ('Bicycle','Bicycle')
    )

    vehicle_type = models.CharField(
        max_length=20,
        blank = False,
        default = 'Car',
        choices = vehicles,
        # validation = vehicle_type_validate
    )
    parking = (
        ("self","self"),
        ("wallet","wallet")
    )
    parking_type = models.CharField(max_length=10,choices=parking)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField()
    slot = models.PositiveIntegerField(blank=False)

    objects = models.DjongoManager()

    class Meta:
        """Meta definition for Parking."""

        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        """Unicode representation of Parking."""
        return str(self.vehicle_number)

    def __unicode__(self):
        return str(self.vehicle_number)

    meta ={
    }

    # validation for cehicle type selection
class VehicalFees(models.Model):
    vehicles = (
        ("car","car"),
        ("bike","bike"),
        ("cycle","cycle")
    )
    vehicle_type = models.CharField(max_length=10,choices=vehicles)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.vehicle_type +"--"+str(self.cost)

class DriverFees(models.Model):
    drivers = (
        ("owner","owner"),
        ("policeman","policeman"),
        ("driver","driver")
    )
    driver_type = models.CharField(max_length=10,choices=drivers)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.driver_type+"--"+str(self.cost)

class ParkingFees(models.Model):
    parking = (
        ("self","self"),
        ("wallet","wallet")
        )
    parking_type = models.CharField(max_length=10,choices=parking)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.parking_type+"--"+str(self.cost)