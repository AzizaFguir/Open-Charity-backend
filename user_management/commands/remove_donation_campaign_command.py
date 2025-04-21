from core.models import User
from helpers import IpfsHelper
import logging

class RemoveDonationCampaignCommand:

    def __init__(self, walletAddress, campaignId, ipfsController):
        self.walletAddress = walletAddress
        self.campaignId = campaignId
        self.ipfsController = ipfsController

    def execute(self):
        try:
            # Retrieve user data from IPFS
            userData = self.ipfsController.getUserIpfsData(self.walletAddress)
            
            # Create a User object with the retrieved data
            user = User(userData["walletAddress"], userData["username"], userData["profilePic"],
                        userData["donations"], userData["donationCampaigns"])
            
            # Remove the donation campaign from the user
            user.removeDonationCampaign(self.campaignId)

            # Upload updated user data to IPFS
            response = IpfsHelper.uploadData(user.getData())
            
            # Log the response from IPFS upload to understand its structure
            logging.info(f"IPFS upload response: {response}")
            
            # Safely access 'IpfsHash' and raise an error if it's missing
            ipfsHash = response.get("IpfsHash")
            if not ipfsHash:
                raise ValueError("Failed to retrieve 'IpfsHash' from IPFS response.")
            
            # Update the user's IPFS record with the new IPFS hash
            self.ipfsController.updateUserIpfsRecord(user.getWalletAddress(), ipfsHash)

            # Return the updated user data
            return user.getData()

        except Exception as e:
            # Handle exceptions and log the error
            logging.error(f"Error occurred in RemoveDonationCampaignCommand: {e}")
            raise  # Re-raise the exception after logging it

