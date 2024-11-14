from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    USER_TYPE = (
        ("doctor", "doctor"),
        ("patient", "patient")
    )
    username = None
    phone_number = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPE)
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number



class DoctorSpecialize(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialize = models.ForeignKey(DoctorSpecialize, 
                                   on_delete=models.SET_NULL, 
                                   null=True, blank=True)
    photo = models.ImageField(upload_to='images/')
    certificate = models.FileField(upload_to='certificates/')


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
