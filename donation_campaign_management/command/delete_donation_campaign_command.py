from core.models import DonationCampaign

class DeleteDonationCampaignCommand:
    def __init__(self, id, ipfsController, userController):
        self.id = id
        self.ipfsController = ipfsController
        self.userController = userController

    def execute(self):
        # Fetch campaign data from IPFS
        campaign_data = self.ipfsController.getDonationCampaignIpfsRecord(self.id)

        # Define the allowed keys for filtering
        allowed_keys = ["id", "title", "description", "openStatus", "wallpaper", "beneficiary"]

        # Filter the campaign data to only include the allowed keys
        filtered_data = {k: v for k, v in campaign_data.items() if k in allowed_keys}

        # Check if all required keys are in the filtered data
        missing_keys = [key for key in allowed_keys if key not in filtered_data]

        if missing_keys:
            raise ValueError(f"Missing required fields: {', '.join(missing_keys)}")

        # Proceed to delete campaign from IPFS
        result = self.ipfsController.deleteDonationCampaignIpfsRecord(self.id)

        # If deletion was successful, update user data
        if result["code"] == 200:
            campaign = DonationCampaign(**filtered_data)
            self.userController.removeDonationCampaignFromUser(campaign.getBeneficiary(), campaign.getId())

        return result
