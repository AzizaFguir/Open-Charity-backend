from django.db import models

# Create your models here.


class UserIpfsGateway(models.Model):
    walletAddress = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255) 

class DonationCampaignIpfsGateway(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255) 

class DonationIpfsGateway(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    cid = models.CharField(max_length=255) 

class NotificationIpfsGateway(models.Model):
    cid = models.CharField(max_length=255) 
