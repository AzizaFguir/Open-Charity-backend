from core.models import User, DonationCampaign, Donation
from helpers import IpfsHelper
from ipfs_gateway.controllers import UserIpfsGatewayController
from session_management.controllers import SessionController
from decorators import singleton

@singleton
class UserService:

    def __init__(self, 
        userIpfsGatewayController = UserIpfsGatewayController(),
        sessionController = SessionController()
    ):
        self.userIpfsGatewayController = userIpfsGatewayController
        self.sessionController = sessionController

    def getUser(self, walletAddress: str):
        return self.userIpfsGatewayController.getUserIpfsData(walletAddress)

    def getUsers(self):
        return self.userIpfsGatewayController.getAllUserIpfsData()

    def createUser(self, data):
        user = User(data["walletAddress"], data["username"], data["profilePic"])
        self.userIpfsGatewayController.saveUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])
        return user.getData()

    def updateUser(self, walletAddress: str, data):
        userData = self.userIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])

        user.update(
            username=data["username"], 
            profilePic=data["profilePic"], 
            walletAddress=data["walletAddress"]
        )

        self.userIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()

    def addDonationCampaignToUser(self, walletAddress, donationCamapign: DonationCampaign):
        userData = self.userIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.addDonationCampaign(donationCamapign)
        self.userIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    def removeDonationCampaignFromUser(self, walletAddress, donationCampaignId: str):
        userData = self.userIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.removeDonationCampaign(donationCampaignId)
        self.userIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    def updateUserDonationCampaign(self, walletAddress, donationCamapign: DonationCampaign):
        userData = self.userIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.updateDonationCampaign(donationCamapign)
        self.userIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    def addDonationToUser(self, walletAddress: str, donation: Donation):
        userData = self.userIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.addDonation(donation)
        self.userIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()

    def login(self, data):
        return self.sessionController.addSession(data["walletAddress"], data["signature"])
            
    
    def logout(self, data):
        return self.sessionController.removeSession(data["sessionToken"])