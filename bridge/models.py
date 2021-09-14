from django.db import models

class Bridge(models.Model):
    bridgeName = models.CharField(max_length=60)
    bridgeDescription = models.TextField()
    bridgeImg = models.ImageField(upload_to='bridge_img')

    def __str__(self):
        return f'{self.bridgeName}'
    
    def save(self, *args, **kwargs):
        super(Bridge, self).save(*args, **kwargs)
