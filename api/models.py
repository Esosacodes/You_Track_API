from django.db import models
from  django.contrib.auth import User
from  django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=500, blank=False)
    name = models.CharField(max_length=30, blank=False)
    password = models.TextField(min_length=6, blank=False)


        

