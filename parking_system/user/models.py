from djongo import models
from django.utils.translation import gettext_lazy as _

# from django.db import models
# Create your models here.
class Account(models.Model):
    #role choices
    roles = [
        ("driver","driver"),
         ("police","police"),
          ("owner","owner"),
    ]
    """Model definition for User."""

    Username = models.CharField(max_length=100,blank=False,null=False)
    role = models.CharField(max_length=10,choices=roles,blank=False,default="driver")
    email = models.EmailField(unique=True,blank=False,default="email")

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return self.Username
