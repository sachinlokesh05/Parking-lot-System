from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegisterUserSerializer
from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from .UseException import RoleNotExist
class Register(APIView):
    queryset = User
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(request.data['roles'])

        try:
            print(request.data['roles'])
            group = Group.objects.get(name=request.data['roles'])
            print(group)
            user.groups.add(group)
        except Exception :
            raise RoleNotExist
        return Response(data="Succefully Registered",status=status.HTTP_201_CREATED)