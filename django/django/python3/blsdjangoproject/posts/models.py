from distutils.command.upload import upload
from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')

def __str__(self):
    return self.title
