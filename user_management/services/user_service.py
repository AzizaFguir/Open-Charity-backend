from user_management.commands.create_user_command import CreateUserCommand
from user_management.commands.update_user_command import UpdateUserCommand
from user_management.commands.login_user_command import LoginUserCommand
from user_management.commands.logout_user_command import LogoutUserCommand
from user_management.commands.add_donation_to_user_command import AddDonationToUserCommand
from user_management.commands.add_donation_campaign_command import AddDonationCampaignCommand
from user_management.commands.remove_donation_campaign_command import RemoveDonationCampaignCommand
from user_management.commands.update_donation_campaign_command import UpdateDonationCampaignCommand

from ipfs_gateway.controllers import UserIpfsGatewayController
from session_management.controllers import SessionController
from decorators import singleton

@singleton
class UserService:

    def __init__(self, 
        userIpfsGatewayController=UserIpfsGatewayController(),
        sessionController=SessionController()
    ):
        self.userIpfsGatewayController = userIpfsGatewayController
        self.sessionController = sessionController

    def getUser(self, walletAddress):
        return self.userIpfsGatewayController.getUserIpfsData(walletAddress)

    def getUsers(self):
        return self.userIpfsGatewayController.getAllUserIpfsData()

    def createUser(self, data):
        return CreateUserCommand(data, self.userIpfsGatewayController).execute()

    def updateUser(self, walletAddress, data):
        return UpdateUserCommand(walletAddress, data, self.userIpfsGatewayController).execute()

    def addDonationToUser(self, walletAddress, donation):
        return AddDonationToUserCommand(walletAddress, donation, self.userIpfsGatewayController).execute()

    def addDonationCampaignToUser(self, walletAddress, campaign):
        return AddDonationCampaignCommand(walletAddress, campaign, self.userIpfsGatewayController).execute()

    def removeDonationCampaignFromUser(self, walletAddress, campaignId):
        return RemoveDonationCampaignCommand(walletAddress, campaignId, self.userIpfsGatewayController).execute()

    def updateUserDonationCampaign(self, walletAddress, campaign):
        return UpdateDonationCampaignCommand(walletAddress, campaign, self.userIpfsGatewayController).execute()

    def login(self, data):
        return LoginUserCommand(data, self.sessionController).execute()

    def logout(self, data):
        return LogoutUserCommand(data, self.sessionController).execute()
