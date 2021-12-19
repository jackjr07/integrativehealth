from django.db import models
from django.utils import timezone
from django.urls import reverse

class Program(models.Model):
    programName = models.CharField(max_length=60, verbose_name="Name of the program")
    programDescription = models.TextField(verbose_name="Description of the program")
    programUrl = models.CharField(max_length=60, verbose_name="Program name without space")
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.programName}'

    def get_absolute_url(self):
        return reverse('program-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super(Program, self).save(*args, **kwargs)

class SubProgram(models.Model):
    subprogramName = models.CharField(max_length=100, verbose_name="Name of the sub-program")
    subprogramDescription = models.TextField(verbose_name="Description of this sub-program")
    datePosted = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.subprogramName}'

    def save(self, *args, **kwargs):
        super(SubProgram, self).save(*args, **kwargs)

class ConfirmedCase(models.Model):
    yesno = [('no', "Waiting"), ('yes', "Contacted")]
    patName = models.CharField(max_length=100, verbose_name="Patient Name")
    patProgram = models.CharField(max_length=100, verbose_name="Program Name")
    patChecked = models.CharField(max_length=5, choices=yesno, default='no')
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.patName}'

    def save(self, *args, **kwargs):
        super(ConfirmedCase, self).save(*args, **kwargs)
