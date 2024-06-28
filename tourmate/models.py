from django.db import models

# Create your models here.
class Tour(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
