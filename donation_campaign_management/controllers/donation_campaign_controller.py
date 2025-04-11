from ..services import DonationCampaignService
from core.models import Donation
from common import singleton


@singleton
class DonationCampaignController:

    def __init__(self, donationCampaignService = DonationCampaignService()):
        self.donationCampaignService = donationCampaignService


    def getDonationCampaigns(self):
        return self.donationCampaignService.getDonationCampaigns() 

    def getDonationCampaign(self, id: str):
        return self.donationCampaignService.getDonationCampaign(id)

    def createDonationCampaign(self, data):
        return self.donationCampaignService.createDonationCampaign(data)
    
    def updateDonationCampaign(self, data, id: str):
        return self.donationCampaignService.updateDonationCampaign(data, id)

    def deleteDonationCampaign(self, id: str):
        return self.donationCampaignService.deleteDonationCampaign(id)

    def addDonationToCampaign(self, donation: Donation, id: str):
        return self.donationCampaignService.addDonationToCampaign(donation, id)

