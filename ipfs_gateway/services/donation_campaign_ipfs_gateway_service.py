from ..models import DonationCampaignIpfsGateway
from helpers import IpfsHelper
from common import singleton

@singleton
class DonationCampaignIpfsGatewayService:
    
    def saveDonationCampaignIpfsRecord(self, id, cid):
        donationCampaignIpfsRecord = DonationCampaignIpfsGateway(id=id, cid=cid)
        donationCampaignIpfsRecord.save()
        return True

    def deleteDonationCampaignIpfsRecord(self, id):
        DonationCampaignIpfsGateway.objects.filter(id=id).delete()
        return {"code": 200}

    def updateDonationCampaignIpfsRecord(self, id, cid):
        donationCampaignIpfsRecord = DonationCampaignIpfsGateway.objects.get(id=id)
        donationCampaignIpfsRecord.cid = cid
        donationCampaignIpfsRecord.save()
        return True

    def getDonationCampaignIpfsRecord(self, id):
        try:
            return IpfsHelper.fetchData(DonationCampaignIpfsGateway.objects.get(id = id).cid)
        except DonationCampaignIpfsGateway.DoesNotExist:
            return {
                "id": "",
                "title": "",
                "description": "",
                "beneficiary": "",
                "donations": {},
                "openStatus": "",
                "dateCreated": ""
            }

    def getDonationCampaignsIpfsRecord(self):
        return [IpfsHelper.fetchData(donationCampaign.cid) for donationCampaign in DonationCampaignIpfsGateway.objects.all()]