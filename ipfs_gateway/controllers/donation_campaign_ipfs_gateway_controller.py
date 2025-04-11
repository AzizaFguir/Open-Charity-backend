from ..services import DonationCampaignIpfsGatewayService

class DonationCampaignIpfsGatewayController:
    
    @staticmethod
    def saveDonationCampaignIpfsRecord(id, cid):
        return DonationCampaignIpfsGatewayService.saveDonationCampaignIpfsRecord(id, cid)

    @staticmethod
    def deleteDonationCampaignIpfsRecord(id):
        return DonationCampaignIpfsGatewayService.deleteDonationCampaignIpfsRecord(id)

    @staticmethod
    def updateDonationCampaignIpfsRecord(id, cid):
        return DonationCampaignIpfsGatewayService.updateDonationCampaignIpfsRecord(id, cid)

    @staticmethod
    def getDonationCampaignsIpfsRecord():
        return DonationCampaignIpfsGatewayService.getDonationCampaignsIpfsRecord()

    @staticmethod
    def getDonationCampaignIpfsRecord(id):
        return DonationCampaignIpfsGatewayService.getDonationCampaignIpfsRecord(id)