from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .options import *

class vascularBridgeRegister(models.Model):
    patientName = models.ForeignKey(User, on_delete=models.CASCADE)
    staffName = models.CharField(max_length=100, choices=STAFFLIST)
    nurseManager= models.CharField(max_length=60, choices=NSMANAGER)
    healthInsurance = models.CharField(max_length=30, choices=INSURANCE)
    educationLevel = models.CharField(max_length=20, choices=EDUCATION)    
    occupation = models.CharField(max_length=30, choices=OCCUPATION)

