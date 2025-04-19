from ..services import UserService, IUserService
from core.models import DonationCampaign, Donation
from decorators import singleton

@singleton
class UserController:

    def __init__(
            self, 
            userService: IUserService = UserService()
    ):
        self.userService = userService

    def getUser(self, walletAddress: str):
        return self.userService.getUser(walletAddress)

    def getUsers(self):
        return self.userService.getUsers()

    def createUser(self, data):
        return self.userService.createUser(data)

    def updateUser(self, walletAddress, data):
        return self.userService.updateUser(walletAddress, data)

    def addDonationCampaignToUser(self, walletAddress, donationCamapign: DonationCampaign):
        return self.userService.addDonationCampaignToUser(walletAddress, donationCamapign)
    
    def removeDonationCampaignFromUser(self, walletAddress, donationCampaignId: str):
        return self.userService.removeDonationCampaignFromUser(walletAddress, donationCampaignId)

    def updateUserDonationCampaign(self, walletAddress, donationCampaign: DonationCampaign):
        return self.userService.updateUserDonationCampaign(walletAddress, donationCampaign)
    
    def addDonationToUser(self, walletAddress: str, donation: Donation):
        return self.userService.addDonationToUser(walletAddress, donation)

    def login(self, data):
        return self.userService.login(data)

    def logout(self, data):
        return self.userService.logout(data)
    
    