from core.models import Donation
from helpers import StringHelper, IpfsHelper

class AddDonationCommand:

    def __init__(self, donationData, ipfsGatewayController, campaignController, userController):
        self.donationData = donationData
        self.ipfsGatewayController = ipfsGatewayController
        self.campaignController = campaignController
        self.userController = userController

    def execute(self):
        donation = Donation(
            StringHelper.generateRandomString(), 
            self.donationData["donor"], 
            self.donationData["donationCampaignId"],
            self.donationData["amount"]
        )

        self.ipfsGatewayController.saveDonationIpfsRecord(
            donation.getId(),
            IpfsHelper.uploadData(donation.getData())["IpfsHash"]
        )

        self.campaignController.addDonationToCampaign(donation, donation.getDonationCampaign())
        self.userController.addDonationToUser(donation.getDonor(), donation)

        return donation.getData()
