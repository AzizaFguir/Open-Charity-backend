
from ..models import DonationIpfsGateway
from helpers import IpfsHelper
from decorators import singleton

@singleton
class DonationIpfsGatewayService:
    
    def saveDonationIpfsRecord(self, id: str, cid: str):
       donationIpfsGateway = DonationIpfsGateway(id=id, cid=cid)
       donationIpfsGateway.save()
       return True


    def getDonation(self, id):
        try:
            return IpfsHelper.fetchData(DonationIpfsGateway.objects.get(id=id).cid)
        except DonationIpfsGateway.DoesNotExist:
            return {
                "amount": "",
                "dateDonated": "",
                "donationCampaignId": "",
                "donor": ""
            }