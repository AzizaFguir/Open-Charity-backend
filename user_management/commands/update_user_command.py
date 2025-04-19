from core.models import User
from helpers import IpfsHelper


class UpdateUserCommand:

    def __init__(self, walletAddress, data, ipfsController):
        self.walletAddress = walletAddress
        self.data = data
        self.ipfsController = ipfsController

    def execute(self):
        # Fetch current user data from IPFS
        userData = self.ipfsController.getUserIpfsData(self.walletAddress)
        
        # Reconstruct the User object
        user = User(
            userData["walletAddress"],
            userData["username"],
            userData["profilePic"],
            userData["donations"],
            userData["donationCampaigns"]
        )

        # Update user with new data
        user.update(
            username=self.data["username"],
            profilePic=self.data["profilePic"],
            walletAddress=self.data["walletAddress"]
        )

        # Upload updated user data to IPFS
        upload_result = IpfsHelper.uploadData(user.getData())

        if not isinstance(upload_result, dict) or "IpfsHash" not in upload_result:
            raise ValueError(f"IPFS upload failed or response malformed: {upload_result}")

        ipfsHash = upload_result["IpfsHash"]

        # Update IPFS record for the user
        self.ipfsController.updateUserIpfsRecord(user.getWalletAddress(), ipfsHash)

        # Return updated user data
        return user.getData()
