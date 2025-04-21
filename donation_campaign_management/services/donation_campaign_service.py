from ..command.create_donation_campaign_command import CreateDonationCampaignCommand
from ..command.update_donation_campaign_command import UpdateDonationCampaignCommand
from ..command.delete_donation_campaign_command import DeleteDonationCampaignCommand
from ..command.add_donation_to_campaign_command import AddDonationToCampaignCommand
from ipfs_gateway.controllers import DonationCampaignIpfsGatewayController
from user_management.controllers import UserController
from decorators import singleton


@singleton
class DonationCampaignService:

    def __init__(self, ipfsController=DonationCampaignIpfsGatewayController(), userController=UserController()):
        self.ipfsController = ipfsController
        self.userController = userController

    def getDonationCampaigns(self):
        return self.ipfsController.getDonationCampaignsIpfsRecord()

    def getDonationCampaign(self, id):
        return self.ipfsController.getDonationCampaignIpfsRecord(id)

    def createDonationCampaign(self, data):
        return CreateDonationCampaignCommand(data, self.ipfsController, self.userController).execute()

    def updateDonationCampaign(self, data, id):
        return UpdateDonationCampaignCommand(id, data, self.ipfsController, self.userController).execute()

    def deleteDonationCampaign(self, id):
        return DeleteDonationCampaignCommand(id, self.ipfsController, self.userController).execute()

    def addDonationToCampaign(self, donation, id):
        return AddDonationToCampaignCommand(id, donation, self.ipfsController, self.userController).execute()
