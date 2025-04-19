from abc import ABC
from core.models import DonationCampaign, Donation


class IUserService(ABC):

    def getUser(self, walletAddress: str): pass

    def getUsers(self): pass

    def createUser(self, data): pass

    def updateUser(self, walletAddress: str, data): pass
        
    def addDonationCampaignToUser(self, walletAddress, donationCamapign: DonationCampaign): pass

    def removeDonationCampaignFromUser(self, walletAddress, donationCampaignId: str): pass
    
    def updateUserDonationCampaign(self, walletAddress, donationCamapign: DonationCampaign): pass
    
    def addDonationToUser(self, walletAddress: str, donation: Donation): pass

    def login(self, data): pass
    
    def logout(self, data): pass