from core.models import DonationCampaign, Donation
from helpers import IpfsHelper, StringHelper
from ipfs_gateway.controllers import DonationCampaignIpfsGatewayController
from user_management.controllers import UserController
from .i_donation_campaign_service import IDonationCampaignService
from decorators import singleton


@singleton
class DonationCampaignService(IDonationCampaignService): 

    def __init__(
        self,
        donationCampaignIpfsGatewayController = DonationCampaignIpfsGatewayController(),
        userController = UserController()
    ):
        self.donationCampaignIpfsGatewayController = donationCampaignIpfsGatewayController
        self.userController = userController
    
    def getDonationCampaigns(self):
        return self.donationCampaignIpfsGatewayController.getDonationCampaignsIpfsRecord()

    def getDonationCampaign(self, id):
        return self.donationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
    

    def createDonationCampaign(self, data):
        donationCampaign = DonationCampaign(StringHelper.generateRandomString(), data["title"], data["description"], data["wallpaper"], data["beneficiary"])
        self.donationCampaignIpfsGatewayController.saveDonationCampaignIpfsRecord(donationCampaign.getId(), IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        self.userController.addDonationCampaignToUser(data["beneficiary"], donationCampaign)
        return donationCampaign.getData()

    
    def updateDonationCampaign(self, data, id):
        donationCampaignData = self.donationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
        
        donationCampaign = DonationCampaign(
            donationCampaignData["id"],
            donationCampaignData["title"],
            donationCampaignData["description"],
            donationCampaignData["wallpaper"],
            donationCampaignData["beneficiary"],
            donationCampaignData["donations"],
            donationCampaignData["openStatus"]
        )

        donationCampaign.update(data["title"], data["description"], data["openStatus"], data["wallpaper"])
        self.donationCampaignIpfsGatewayController.updateDonationCampaignIpfsRecord(id, IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        self.userController.updateUserDonationCampaign(donationCampaign.getBeneficiary(), donationCampaign)

        return donationCampaign.getData()

    def deleteDonationCampaign(self, id):
        donationCampaignData = self.donationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
        result = self.donationCampaignIpfsGatewayController.deleteDonationCampaignIpfsRecord(id)

        if(result["code"] == 200):
            donationCampaign = DonationCampaign(
                donationCampaignData["id"],
                donationCampaignData["title"],
                donationCampaignData["description"],
                donationCampaignData["wallpaper"],
                donationCampaignData["beneficiary"],
                donationCampaignData["donations"],
                donationCampaignData["openStatus"]
            )

            self.userController.removeDonationCampaignFromUser(donationCampaign.getBeneficiary(), donationCampaign.getId())

        
        return result
    
    def addDonationToCampaign(self, donation: Donation, id: str):
        donationCampaignData = self.donationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)

        donationCampaign = DonationCampaign(
            donationCampaignData["id"],
            donationCampaignData["title"],
            donationCampaignData["description"],
            donationCampaignData["wallpaper"],
            donationCampaignData["beneficiary"],
            donationCampaignData["donations"],
            donationCampaignData["openStatus"]
        )  

        donationCampaign.addDonation(donation)
        self.donationCampaignIpfsGatewayController.updateDonationCampaignIpfsRecord(id, IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        self.userController.updateUserDonationCampaign(donationCampaign.getBeneficiary(), donationCampaign)

        return donationCampaign.getData()



        

        