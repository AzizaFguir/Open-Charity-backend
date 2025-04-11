from django.db import models

# Create your models here.

class Session(models.Model):
    sessionToken = models.CharField(max_length=255, primary_key=True)
    walletAddress = models.CharField(max_length=255)