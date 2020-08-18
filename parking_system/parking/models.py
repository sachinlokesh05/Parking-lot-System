from djongo import models

# Create your models here.
class Parking(models.Model):
    """Model definition for Parking."""
    # vehicle_type 
    vehicles = [
        
        ('2-wheelers','2-wheelers'),
        ('4-wheelers','4-wheelers'),
        ('bicycle','bicycle'),

    ]
    
    vehicel_number = models.CharField(max_length=10,unique=True,editable=False)
    vehicle_type = models.CharField(max_length=10,choices=vehicles,help_text='select your vehicle type')
    entry_time = models.DateTimeField(editable=False)
    end_time = models.DateTimeField(editable=False)


    class Meta:
        """Meta definition for Parking."""

        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        """Unicode representation of Parking."""
        pass
