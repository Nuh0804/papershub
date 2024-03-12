from django.db import models
from django.contrib.auth.models import AbstractUser
from .usermanage import MyUserManager
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length= 255)
    last_name =  models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 255)
    phone_number = models.CharField(unique=True, max_length= 10)
    password = models.CharField(max_length = 255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()
    def __str__(self):
        return self.email
