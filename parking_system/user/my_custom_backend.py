from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from user.UseException import SomeOneIsLoggedInAlready
from rest_framework.response import Response


class EmailOrUsernameModelBackend(BaseBackend):

    def authenticate(self, request,username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
             kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if getattr(user, 'is_active', False) and user.check_password(password) :
                    return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None