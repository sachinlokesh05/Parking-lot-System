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
from django.contrib.auth import login

class Register(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            group = Group.objects.get(name=request.data['roles'])
        except Exception :
            return Response(data="Role Does not Exist",status=status.HTTP_404_NOT_FOUND)
        user = serializer.save()    
        user.groups.add(group)    
        return Response(data="Succefully Registered",status=status.HTTP_201_CREATED)

