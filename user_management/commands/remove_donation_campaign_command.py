from core.models import User
from helpers import IpfsHelper

class RemoveDonationCampaignCommand:

    def __init__(self, walletAddress, campaignId, ipfsController):
        self.walletAddress = walletAddress
        self.campaignId = campaignId
        self.ipfsController = ipfsController

    def execute(self):
        userData = self.ipfsController.getUserIpfsData(self.walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"],
                    userData["donations"], userData["donationCampaigns"])
        user.removeDonationCampaign(self.campaignId)
        ipfsHash = IpfsHelper.uploadData(user.getData())["IpfsHash"]
        self.ipfsController.updateUserIpfsRecord(user.getWalletAddress(), ipfsHash)
        return user.getData()
