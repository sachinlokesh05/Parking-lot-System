from djongo import models
from django.contrib.auth.models import User
import mongoengine
class Log(models.Model):
    """Model definition for Log."""

    entry_time = models.DateTimeField(verbose_name="Entry time",editable=False,default="")
    exit_time = models.DateTimeField(verbose_name="Exit time",editable=False,default="")

    class Meta:
        """Meta definition for Log."""

        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
        abstract = True

    def __str__(self):
        """Unicode representation of Log."""
        return str(self.entry_time)+" to "+str(self.exit_time)


 
class Parking(models.Model):
    """Model definition for Parking."""
    _id = models.ObjectIdField()
    user_details = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20,blank = False)

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
    logs =  models.EmbeddedField(model_container=Log,null=True)
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
        'ordering': ['-created_at'],

    }

    # validation for cehicle type selection
   
