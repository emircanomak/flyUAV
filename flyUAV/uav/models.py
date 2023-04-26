from django.db import models

# Create your models here.

class uavModel(models.Model):
    name=models.CharField(max_length=40)
    brand=models.CharField(max_length=40)
    weight=models.PositiveBigIntegerField(default=0)
    category=models.CharField(max_length=50)
    date=models.DateField()