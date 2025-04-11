from core.models import User, DonationCampaign, Donation
from helpers import IpfsHelper
from ipfs_gateway.controllers import UserIpfsGatewayController
from session_management.controllers import SessionController

class UserService:

    @staticmethod
    def getUser(walletAddress: str):
        return UserIpfsGatewayController.getUserIpfsData(walletAddress)

    @staticmethod
    def getUsers():
        return UserIpfsGatewayController.getAllUserIpfsData()

    @staticmethod
    def createUser(data):
        user = User(data["walletAddress"], data["username"], data["profilePic"])
        UserIpfsGatewayController.saveUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])
        return user.getData()

    @staticmethod
    def updateUser(walletAddress: str, data):
        userData = UserIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])

        user.update(
            username=data["username"], 
            profilePic=data["profilePic"], 
            walletAddress=data["walletAddress"]
        )

        UserIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()

    @staticmethod
    def addDonationCampaignToUser(walletAddress, donationCamapign: DonationCampaign):
        userData = UserIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.addDonationCampaign(donationCamapign)
        UserIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    @staticmethod
    def removeDonationCampaignFromUser(walletAddress, donationCampaignId: str):
        userData = UserIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.removeDonationCampaign(donationCampaignId)
        UserIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    @staticmethod
    def updateUserDonationCampaign(walletAddress, donationCamapign: DonationCampaign):
        userData = UserIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.updateDonationCampaign(donationCamapign)
        UserIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()
    
    @staticmethod
    def addDonationToUser(walletAddress: str, donation: Donation):
        userData = UserIpfsGatewayController.getUserIpfsData(walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"], userData["donations"], userData["donationCampaigns"])
        user.addDonation(donation)
        UserIpfsGatewayController.updateUserIpfsRecord(user.getWalletAddress(), IpfsHelper.uploadData(user.getData())["IpfsHash"])

        return user.getData()

    @staticmethod
    def login(data):
        return SessionController.addSession(data["walletAddress"], data["signature"])
            
    
    @staticmethod
    def logout(data):
        return SessionController.removeSession(data["sessionToken"])