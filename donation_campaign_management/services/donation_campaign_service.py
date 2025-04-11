from core.models import DonationCampaign, Donation
from helpers import IpfsHelper, StringHelper
from ipfs_gateway.controllers import DonationCampaignIpfsGatewayController
from userManagement.controllers import UserController


class DonationCampaignService: 
    
    def getDonationCampaigns():
        return DonationCampaignIpfsGatewayController.getDonationCampaignsIpfsRecord()

    def getDonationCampaign(id):
        return DonationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
    

    def createDonationCampaign(data):
        donationCampaign = DonationCampaign(StringHelper.generateRandomString(), data["title"], data["description"], data["wallpaper"], data["beneficiary"])
        DonationCampaignIpfsGatewayController.saveDonationCampaignIpfsRecord(donationCampaign.getId(), IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        UserController.addDonationCampaignToUser(data["beneficiary"], donationCampaign)
        return donationCampaign.getData()

    
    def updateDonationCampaign(data, id):
        donationCampaignData = DonationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
        
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
        DonationCampaignIpfsGatewayController.updateDonationCampaignIpfsRecord(id, IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        UserController.updateUserDonationCampaign(donationCampaign.getBeneficiary(), donationCampaign)

        return donationCampaign.getData()

    def deleteDonationCampaign(id):
        donationCampaignData = DonationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)
        result = DonationCampaignIpfsGatewayController.deleteDonationCampaignIpfsRecord(id)

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

            UserController.removeDonationCampaignFromUser(donationCampaign.getBeneficiary(), donationCampaign.getId())

        
        return result
    
    @staticmethod
    def addDonationToCampaign(donation: Donation, id: str):
        donationCampaignData = DonationCampaignIpfsGatewayController.getDonationCampaignIpfsRecord(id)

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
        DonationCampaignIpfsGatewayController.updateDonationCampaignIpfsRecord(id, IpfsHelper.uploadData(donationCampaign.getData())["IpfsHash"])
        UserController.updateUserDonationCampaign(donationCampaign.getBeneficiary(), donationCampaign)

        return donationCampaign.getData()



        

        