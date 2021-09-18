from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .options import *

class limbIndexSym(models.Model):
    limbSymptoms = models.CharField(max_length=100)

    def __str__(self):
        return self.limbSymptoms

class limbIndexRutherford(models.Model):
    limbRutherford = models.CharField(max_length=100)

    def __str__(self):
        return self.limbRutherford

class limbIndexDiagnosis(models.Model):
    limbDiagnosis = models.CharField(max_length=30)

    def __str__(self):
        return self.limbDiagnosis

class limbPlansurgical(models.Model):
    surgical = models.CharField(max_length=30)

    def __str__(self):
        return self.surgical



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
    leftLimbIndex = models.CharField(max_length=100)
    leftLimbRutherford = models.CharField(max_length=100)
    rightLimbIndex = models.CharField(max_length=100)
    rightLimbRutherford = models.CharField(max_length=100)
    priorintervention = models.CharField(max_length=10, choices=YN)
    leftLimbDiagnosis = models.CharField(max_length=20)
    rightLimbDiagnosis = models.CharField(max_length=20)
    nonInvasiveTest = models.CharField(max_length=10, choices=COMPLETED)
    woundScore = models.CharField(max_length=5, choices=LEVELS, help_text=WOUNDHELPTEXT)
    ischaemiaScore = models.CharField(max_length=5, choices=LEVELS)
    footinfectionScore = models.CharField(max_length=5, choices=LEVELS)
    planSurgical = models.CharField(max_length=10)




