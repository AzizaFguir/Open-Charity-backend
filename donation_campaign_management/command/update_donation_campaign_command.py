from core.models import DonationCampaign
from helpers import IpfsHelper

class UpdateDonationCampaignCommand:
    def __init__(self, id, data, ipfsController, userController):
        self.id = id
        self.data = data
        self.ipfsController = ipfsController
        self.userController = userController

    def execute(self):
        # Retrieve original campaign data from IPFS
        campaign_data = self.ipfsController.getDonationCampaignIpfsRecord(self.id)

        # ✅ Only allow keys that match the constructor of DonationCampaign
        allowed_keys = ["id", "title", "description", "openStatus", "wallpaper", "beneficiary"]
        filtered_data = {k: v for k, v in campaign_data.items() if k in allowed_keys}

        # ✅ Create the campaign instance safely
        campaign = DonationCampaign(**filtered_data)

        # ✅ Update the campaign object with new data
        campaign.update(
            self.data["title"],
            self.data["description"],
            self.data["openStatus"],
            self.data["wallpaper"]
        )

        # ✅ Save updated data to IPFS and update references
        ipfs_hash = IpfsHelper.uploadData(campaign.getData())["IpfsHash"]
        self.ipfsController.updateDonationCampaignIpfsRecord(self.id, ipfs_hash)
        self.userController.updateUserDonationCampaign(campaign.getBeneficiary(), campaign)

        # ✅ Return updated data
        return campaign.getData()
