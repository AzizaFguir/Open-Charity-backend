from core.models import User
from helpers import IpfsHelper

class AddDonationCampaignCommand:

    def __init__(self, walletAddress, campaign, ipfsController):
        self.walletAddress = walletAddress
        self.campaign = campaign
        self.ipfsController = ipfsController

    def execute(self):
        userData = self.ipfsController.getUserIpfsData(self.walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"],
                    userData["donations"], userData["donationCampaigns"])
        user.addDonationCampaign(self.campaign)
        ipfsHash = IpfsHelper.uploadData(user.getData())["IpfsHash"]
        self.ipfsController.updateUserIpfsRecord(user.getWalletAddress(), ipfsHash)
        return user.getData()
