from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length= 255)
    last_name =  models.CharField(max_length= 255)
    username =  models.CharField(unique=True, max_length= 255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length= 10)

    def __str__(self):
        return self.username
