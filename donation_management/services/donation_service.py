from core.models import Donation
from helpers import StringHelper, IpfsHelper
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
        donation = Donation(
            StringHelper.generateRandomString(), 
            donationData["donor"], 
            donationData["donationCampaignId"],
            donationData['amount']
        )

        self.donationIpfsGatewayController.saveDonationIpfsRecord(
            donation.getId(),
            IpfsHelper.uploadData(donation.getData())["IpfsHash"]
        )

        self.__donationCampaignController.addDonationToCampaign(donation, donation.getDonationCampaign())
        self.__userController.addDonationToUser(donation.getDonor(), donation)

        return donation.getData()
        