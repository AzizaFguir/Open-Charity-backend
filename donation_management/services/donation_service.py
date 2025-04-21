from donation_management.commands.add_donation_command import AddDonationCommand
from donation_campaign_management.controllers import DonationCampaignController
from user_management.controllers import UserController
from ipfs_gateway.controllers import DonationIpfsGatewayController

class DonationService:

    def __init__(
        self,
        donationIpfsGatewayController = DonationIpfsGatewayController(),
        donationCampaignController = DonationCampaignController(),
        userController = UserController()
    ):
        self.donationIpfsGatewayController = donationIpfsGatewayController
        self.donationCampaignController = donationCampaignController
        self.userController = userController

    def addDonation(self, donationData: dict):
        return AddDonationCommand(
            donationData,
            self.donationIpfsGatewayController,
            self.donationCampaignController,
            self.userController
        ).execute()
