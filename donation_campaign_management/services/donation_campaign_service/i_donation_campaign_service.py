from abc import ABC
from core.models import Donation


class IDonationCampaignService(ABC):

    def getDonationCampaigns(self): pass

    def getDonationCampaign(self, id: str): pass

    def createDonationCampaign(self, data): pass
    
    def updateDonationCampaign(self, data, id: str): pass

    def deleteDonationCampaign(self, id: str): pass

    def addDonationToCampaign(self, donation: Donation, id: str): pass