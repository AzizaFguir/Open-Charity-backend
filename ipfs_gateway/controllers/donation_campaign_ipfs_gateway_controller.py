from ..services import DonationCampaignIpfsGatewayService
from decorators import singleton


@singleton
class DonationCampaignIpfsGatewayController:

    def __init__(
        self,
        donationCampaignIpfsGatewayService = DonationCampaignIpfsGatewayService()
    ):
        self.donationCampaignIpfsGatewayService = donationCampaignIpfsGatewayService
    
    def saveDonationCampaignIpfsRecord(self, id, cid):
        return self.donationCampaignIpfsGatewayService.saveDonationCampaignIpfsRecord(id, cid)

    def deleteDonationCampaignIpfsRecord(self, id):
        return self.donationCampaignIpfsGatewayService.deleteDonationCampaignIpfsRecord(id)

    def updateDonationCampaignIpfsRecord(self, id, cid):
        return self.donationCampaignIpfsGatewayService.updateDonationCampaignIpfsRecord(id, cid)

    def getDonationCampaignsIpfsRecord(self):
        return self.donationCampaignIpfsGatewayService.getDonationCampaignsIpfsRecord()

    def getDonationCampaignIpfsRecord(self, id):
        return self.donationCampaignIpfsGatewayService.getDonationCampaignIpfsRecord(id)