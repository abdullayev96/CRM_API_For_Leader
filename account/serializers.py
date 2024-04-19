from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password


#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=70, min_length=6, write_only=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'password', 'is_staff']
#
#
#
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         username = attrs.get('username', '')
#         if not username.isalnum():
#             raise serializers.ValidationError(
#                 self.default_error_messages)
#         return attrs
#
#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=70, min_length=6, write_only=True)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(RegisterSerializer, self).create(validated_data)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_staff']



class VerifySerializer(serializers.Serializer):
     email  = serializers.EmailField()
     otp  = serializers.CharField()

     class Meta:
          model = User
          fields = ['email', 'otp']



class LoginSerializer(serializers.ModelSerializer):
     email = serializers.EmailField()
     password  = serializers.CharField()


     class Meta:
          model  = User
          fields = ['email', 'password']


