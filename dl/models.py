from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    id=models.IntegerField(primary_key=True,auto_created=True)
    email=models.EmailField(unique=True,max_length=254)
    mobile=models.CharField(max_length=50,blank=True)
    username=models.CharField(max_length=50,blank=True)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email
