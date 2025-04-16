from ..services import DonationIpfsGatewayService
from decorators import singleton

@singleton
class DonationIpfsGatewayController:

    def __init__(
        self,
        donationIpfsGatewayService = DonationIpfsGatewayService()
    ):
        self.donationIpfsGatewayService = donationIpfsGatewayService

    def saveDonationIpfsRecord(self, id: str, cid: str):
        return self.donationIpfsGatewayService.saveDonationIpfsRecord(id, cid)
