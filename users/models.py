from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User_profile')
    phone = models.CharField(max_length=20,default = "")
    nombre = models.CharField(max_length=20,default = "")
    apellido = models.CharField(max_length=20,default = "")
    correo = models.CharField(max_length=20,default = "")
    profile_image = models.ImageField(upload_to='profile_image',default = "")
