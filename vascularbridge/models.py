from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STAFFLIST = (
        ('napaporn', 'Napaporn'),
        ('ratana', 'Ratana'),
        )

NSMANAGER = (
        ('napaporn', 'Napaporn'),
        ('ratana', 'Ratana'),
        )
INSURANCE = (
    ('1', 'Social Security'),
    ('2', 'Private'),
)
EDUCATION = (
    ('1', 'K1-K6'),
    ('2', 'K6-K12'),
    ('3', 'AS/AA'),
    ('4', 'BS'),
)
class vascularBridgeRegister(models.Model):
    patientName = models.ForeignKey(User, on_delete=models.CASCADE)
    staffName = models.CharField(max_length=100, choices=STAFFLIST)
    nurseManager= models.CharField(max_length=60, choices=NSMANAGER)
    healthInsurance = models.CharField(max_length=30, choices=INSURANCE)
    educationLevel = models.CharField(max_length=20, choices=EDUCATION)    

