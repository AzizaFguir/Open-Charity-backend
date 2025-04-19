from core.models import DonationCampaign
from helpers import StringHelper, IpfsHelper

class CreateDonationCampaignCommand:
    def __init__(self, data, ipfsController, userController):
        self.data = data
        self.ipfsController = ipfsController
        self.userController = userController

    def execute(self):
        campaign = DonationCampaign(
            StringHelper.generateRandomString(),
            self.data["title"],
            self.data["description"],
            self.data["wallpaper"],
            self.data["beneficiary"]
        )
        ipfs_hash = IpfsHelper.uploadData(campaign.getData())["IpfsHash"]
        self.ipfsController.saveDonationCampaignIpfsRecord(campaign.getId(), ipfs_hash)
        self.userController.addDonationCampaignToUser(self.data["beneficiary"], campaign)
        return campaign.getData()
