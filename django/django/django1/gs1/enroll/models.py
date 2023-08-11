from django.db import models

# Create your models here.
class enroll(models.Model):
    name=models.CharField(max_length=50,blank=False)
    capital=models.CharField(max_length=50)