from django.db import models

# Create your models here.

class Tnh(models.Model):
    temperature = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    meas_date = models.DateTimeField('date measured')

