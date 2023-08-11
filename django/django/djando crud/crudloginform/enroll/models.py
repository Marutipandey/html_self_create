from django.db import models

class User(models.Model):

 username = models.CharField(max_length=30, blank=False, null=False)

 password = models.CharField(max_length=8, blank=False, null=False)