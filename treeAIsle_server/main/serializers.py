from rest_framework import serializers
from .models import User

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