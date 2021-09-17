from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .options import *

class limbIndex(models.Model):
    limbSide = models.CharField(max_length=10, choices=LIMBSIDE) 

    def __str__(self):
        return self.limbSide


class vascularBridgeRegister(models.Model):
    patientName = models.ForeignKey(User, on_delete=models.CASCADE)
    staffName = models.CharField(max_length=100, choices=STAFFLIST)
    nurseManager= models.CharField(max_length=60, choices=NSMANAGER)
    healthInsurance = models.CharField(max_length=30, choices=INSURANCE)
    educationLevel = models.CharField(max_length=20, choices=EDUCATION)    
    occupation = models.CharField(max_length=30, choices=OCCUPATION)
    living = models.CharField(max_length=30, choices=LIVING)
    baseline = models.CharField(max_length=30, choices=BASELINE)
    ql_movement = models.CharField(max_length=30, choices=QL_MOVEMENT)
    ql_selfcare = models.CharField(max_length=30, choices=QL_SELFCARE)
    ql_activities = models.CharField(max_length=30, choices=QL_ACTIVITIES)
    ql_selfcomfortable = models.CharField(max_length=30, choices=QL_SELFCOMFORTABLE)
    ql_anxiety = models.CharField(max_length=30, choices=QL_ANXIETY)
    leftLimbIndex = models.CharField(max_length=30, choices=LIMBSIDE)



