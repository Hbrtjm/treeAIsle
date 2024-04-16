from django.db import models
from datetime import datetime
import hashlib
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

"""
class UserSerializer()
"""


# class TrainingModel(AbstractBaseUser, PermissionsMixin):
#     modelName = models.CharField(max_length=1000, unique=True)


class BaseUserManager(BaseUserManager):

    def create_user(self, email, name, password):
        if not email:
            raise ValueError("No email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        return user


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)  # Storing SHA256 hash
    # is_active = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(default=datetime.now)
    tokens = models.IntegerField(default=0)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    def check_password(self, raw_password):
        # Checking if the provided password matches the stored hash
        hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
        return self.password == hashed_password

    def __str__(self):
        return self.username
