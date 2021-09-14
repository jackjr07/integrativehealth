from django.db import models
from django.utils import timezone
from django.urls import reverse

class Program(models.Model):
    programName = models.CharField(max_length=60, verbose_name="Name of the program")
    programDescription = models.TextField(verbose_name="Description of the program")
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.programName}'

    def get_absolute_url(self):
        return reverse('program-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super(Program, self).save(*args, **kwargs)
