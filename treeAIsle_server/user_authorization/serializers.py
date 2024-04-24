from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class UserCreateSerialzier(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username',
                  'date_of_creation','is_contestant','tokens')
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
class VerifyUserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')