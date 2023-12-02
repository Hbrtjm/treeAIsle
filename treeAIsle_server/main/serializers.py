from rest_framework import serializers
from .models import User

class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','password',
                  'date_of_creation','is_contestant','tokens')