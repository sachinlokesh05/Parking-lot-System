from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegisterUserSerializer
from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import FieldDoesNotExist
from rest_framework.exceptions import NotFound,AuthenticationFailed
from .UseException import RoleNotExist
from .forms import LoginForm
from .my_custom_backend import EmailOrUsernameModelBackend
from django.contrib.auth import login, logout
from user.UseException import LogOutFailed
from user.UseException import SomeOneIsLoggedInAlready

class Register(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            group = Group.objects.get(name=request.data['roles'])
            user = serializer.save()    
            user.groups.add(group)    
            return Response(data="Succefully Registered",status=status.HTTP_201_CREATED)
        except Exception :
            return Response(data="Role Does not Exist",status=status.HTTP_404_NOT_FOUND)
        


@api_view(['POST'])
def Login(request):
    if request.user.is_authenticated:
        return Response(data="User already logged in,Do logout and Try login",status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        form = LoginForm(request.data)
        if form.is_valid():
            auth = EmailOrUsernameModelBackend()
            username = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = auth.authenticate(request,username=username,password=password)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return Response(data="User Login in Succefully",status=status.HTTP_200_OK)
        return Response(data=f"User Login is Failled",status=status.HTTP_400_BAD_REQUEST)
    except form.FieldDoesNotExist:
        return FieldDoesNotExist()
    except Exception as e:
        raise AuthenticationFailed(detail="User Authentication failed",code=404)
@api_view(['GET'])
def Logout(request):
    try:
        logout(request)
        return Response(data="Logged Out Succefully,Thank YOU",status=status.HTTP_200_OK)
    except LogOutFailed:
        return LogOutFailed
