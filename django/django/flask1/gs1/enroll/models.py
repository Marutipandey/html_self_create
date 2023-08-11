from django.db import models

# Create your models here.
class user(models.Model):
    summary=models.CharField(max_length=100,default="hii")
    image=models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.summary()