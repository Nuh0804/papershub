from django.db import models
from django.contrib.auth.models import AbstractUser
from learning_system.models import DegreeProgram
from .usermanage import MyUserManager
# Create your models here.

class User(AbstractUser):
    degree_choices = {
        'CEIT': 'Computer Engineering and Information Technology',
        "CS": "Computer Science",
        "BIT" : "business Information Technology",

    }
    
    first_name = models.CharField(max_length= 255)
    last_name =  models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    username = None
    phone_number = models.CharField(unique=True, max_length= 10)
    password = models.CharField(max_length = 255)
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()
    
    def __str__(self):
        return self.email
