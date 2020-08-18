from djongo import models

# Create your models here.
class User(models.Model):
    """Model definition for User."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass
