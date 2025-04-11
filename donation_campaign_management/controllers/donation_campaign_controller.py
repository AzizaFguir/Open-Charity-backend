from ..services import DonationCampaignService
from core.models import Donation
from common import singleton


@singleton
class DonationCampaignController:


    def getDonationCampaigns(self):
        return DonationCampaignService.getDonationCampaigns() 

    def getDonationCampaign(self, id: str):
        return DonationCampaignService.getDonationCampaign(id)

    def createDonationCampaign(self, data):
        return DonationCampaignService.createDonationCampaign(data)
    
    def updateDonationCampaign(self, data, id: str):
        return DonationCampaignService.updateDonationCampaign(data, id)

    def deleteDonationCampaign(self, id: str):
        return DonationCampaignService.deleteDonationCampaign(id)

    def addDonationToCampaign(self, donation: Donation, id: str):
        return DonationCampaignService.addDonationToCampaign(donation, id)

