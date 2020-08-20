from django.conf import settings
from django.contrib.auth.models import check_password
#from mongoengine.django.auth import check_password
#from django.contrib.auth.hashers import check_password
from .models import MyUser

class EmailAuthBackend(object):

    def authenticate(self, email=None, password=None):
        pass
# ...uh oh, since I'm NOT using one of the usual backends with a pre-existing authenticate()
# method, there ain't a native check_password() function available. Means I have to hash the
# password, etc