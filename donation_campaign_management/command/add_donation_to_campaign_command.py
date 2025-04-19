from helpers import IpfsHelper
from core.models import DonationCampaign

class AddDonationToCampaignCommand:
    def __init__(self, id, donation, ipfsController, userController):
        self.id = id
        self.donation = donation
        self.ipfsController = ipfsController
        self.userController = userController

    def execute(self):
        campaign_data = self.ipfsController.getDonationCampaignIpfsRecord(self.id)
        campaign = DonationCampaign(**campaign_data)
        campaign.addDonation(self.donation)
        ipfs_hash = IpfsHelper.uploadData(campaign.getData())["IpfsHash"]
        self.ipfsController.updateDonationCampaignIpfsRecord(self.id, ipfs_hash)
        self.userController.updateUserDonationCampaign(campaign.getBeneficiary(), campaign)
        return campaign.getData()
