from core.models import User
from helpers import IpfsHelper

class AddDonationToUserCommand:

    def __init__(self, walletAddress, donation, ipfsController):
        self.walletAddress = walletAddress
        self.donation = donation
        self.ipfsController = ipfsController

    def execute(self):
        userData = self.ipfsController.getUserIpfsData(self.walletAddress)
        user = User(userData["walletAddress"], userData["username"], userData["profilePic"],
                    userData["donations"], userData["donationCampaigns"])
        user.addDonation(self.donation)
        ipfsHash = IpfsHelper.uploadData(user.getData())["IpfsHash"]
        self.ipfsController.updateUserIpfsRecord(user.getWalletAddress(), ipfsHash)
        return user.getData()