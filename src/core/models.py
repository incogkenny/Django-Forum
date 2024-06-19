from django.db import models
from django.contrib.auth.models import AbstractUser


# Define custom User Model Class that inherits from Django's AbstractUser
class User(AbstractUser):
    def __str__(self):
        return self.username

    pass
