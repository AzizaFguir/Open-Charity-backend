
from ..models import DonationIpfsGateway
from helpers import IpfsHelper

class DonationIpfsGatewayService:
    
    @staticmethod
    def saveDonationIpfsRecord(id: str, cid: str):
       donationIpfsGateway = DonationIpfsGateway(id=id, cid=cid)
       donationIpfsGateway.save()
       return True


    @staticmethod
    def getDonation(id):
        try:
            return IpfsHelper.fetchData(DonationIpfsGateway.objects.get(id=id).cid)
        except DonationIpfsGateway.DoesNotExist:
            return {
                "amount": "",
                "dateDonated": "",
                "donationCampaignId": "",
                "donor": ""
            }