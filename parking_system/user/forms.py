from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username_or_email = forms.CharField(min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
