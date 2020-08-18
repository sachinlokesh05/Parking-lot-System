from djongo import models

# Create your models here.
class Parking(models.Model):
    """Model definition for Parking."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Parking."""

        verbose_name = 'Parking'
        verbose_name_plural = 'Parkings'

    def __str__(self):
        """Unicode representation of Parking."""
        pass
