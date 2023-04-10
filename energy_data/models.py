from django.db import models

# Create your models here.
class EnergyData(models.Model):
    timestamp = models.DateTimeField()
    energy_reading = models.FloatField()
    location = models.CharField(max_length=100)