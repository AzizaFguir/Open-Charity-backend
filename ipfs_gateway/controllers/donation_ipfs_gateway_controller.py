from ..services import DonationIpfsGatewayService

class DonationIpfsGatewayController:

    @staticmethod
    def saveDonationIpfsRecord(id: str, cid: str):
        return DonationIpfsGatewayService.saveDonationIpfsRecord(id, cid)
