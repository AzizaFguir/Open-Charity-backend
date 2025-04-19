from core.models import User
from helpers import IpfsHelper

class CreateUserCommand:

    def __init__(self, data, ipfsController):
        self.data = data
        self.ipfsController = ipfsController

    def execute(self):
        user = User(self.data["walletAddress"], self.data["username"], self.data["profilePic"])
        ipfsHash = IpfsHelper.uploadData(user.getData())["IpfsHash"]
        self.ipfsController.saveUserIpfsRecord(user.getWalletAddress(), ipfsHash)
        return user.getData()
