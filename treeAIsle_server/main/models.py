from django.db import models
from datetime import datetime
import hashlib
from django.contrib.auth.models import AbstractBaseUser
'''
class UserSerializer()
'''

class TrainingModel(models.Model):
    modelName = models.CharField(max_length=1000, unique=True)

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)  # Storing SHA256 hash
    date_of_creation = models.DateTimeField(default=datetime.now)
    is_contestant = models.BooleanField(default=False)
    tokens = models.IntegerField(default=0)

    def set_password(self, raw_password):
        # Hashing the password using SHA256 before storing
        hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
        self.password = hashed_password

    def check_password(self, raw_password):
        # Checking if the provided password matches the stored hash
        hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
        return self.password == hashed_password

    def __str__(self):
        return self.username

