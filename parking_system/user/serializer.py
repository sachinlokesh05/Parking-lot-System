from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.exceptions import NotAcceptable,NotAcceptable,ValidationError
class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer definition for LoginSerializer."""
    confirm_password =  serializers.CharField(write_only=True)
    roles = serializers.CharField()
    class Meta:
        """Meta definition for LoginSerializer."""

        model = User
        fields = ['username','email','password','roles','confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        user_exits = User.objects.filter(username=value)
        if user_exits :
            raise ValidationError(detail="username already exists",code=403)
        return value

    def validate_email(self, value):
        user_exits = User.objects.filter(email=value)
        if user_exits :
            raise ValidationError(detail="email already exists",code=403)
        return value

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password :
            raise ValidationError(detail="password are not matching",code=403)
        return super(RegisterUserSerializer, self).validate(data)


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user