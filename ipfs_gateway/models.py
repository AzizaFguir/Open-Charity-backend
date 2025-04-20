from django.db import models
from validators import IpfsValidator

# Create your models here.


class UserIpfsGateway(models.Model):
    walletAddress = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255, validators=[IpfsValidator.validateCID]) 

class DonationCampaignIpfsGateway(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255, validators=[IpfsValidator.validateCID]) 

class DonationIpfsGateway(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255, validators=[IpfsValidator.validateCID]) 

class NotificationIpfsGateway(models.Model):
    cid = models.CharField(max_length=255, validators=[IpfsValidator.validateCID]) 

    
