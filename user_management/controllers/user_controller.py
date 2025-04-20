from ..services import UserService, IUserService
from ipfs_gateway.controllers import UserIpfsGatewayController, IUserIpfsGatewayController
from helpers import IpfsHelper

from core.models import DonationCampaign, Donation, User
from decorators import singleton

@singleton
class UserController:

    def __init__(
            self, 
            userService: IUserService = UserService(),
            userIpfsGatewayController: IUserIpfsGatewayController = UserIpfsGatewayController()

    ):
        self.userService = userService
        self.userIpfsGatewayController = userIpfsGatewayController

    def getUser(self, walletAddress: str):
        return self.userService.getUser(walletAddress)

    def getUsers(self):
        return self.userService.getUsers()

    def createUser(self, data):
        user: User = self.userService.createUser(data)
        return self.userIpfsGatewayController.saveUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])
    

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
    
    