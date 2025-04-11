from ..models import DonationCampaignIpfsGateway
from helpers import IpfsHelper

class DonationCampaignIpfsGatewayService:
    
    @staticmethod
    def saveDonationCampaignIpfsRecord(id, cid):
        donationCampaignIpfsRecord = DonationCampaignIpfsGateway(id=id, cid=cid)
        donationCampaignIpfsRecord.save()
        return True

    @staticmethod
    def deleteDonationCampaignIpfsRecord(id):
        DonationCampaignIpfsGateway.objects.filter(id=id).delete()
        return {"code": 200}

    @staticmethod
    def updateDonationCampaignIpfsRecord(id, cid):
        donationCampaignIpfsRecord = DonationCampaignIpfsGateway.objects.get(id=id)
        donationCampaignIpfsRecord.cid = cid
        donationCampaignIpfsRecord.save()
        return True

    @staticmethod
    def getDonationCampaignIpfsRecord(id):
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

    @staticmethod
    def getDonationCampaignsIpfsRecord():
        return [IpfsHelper.fetchData(donationCampaign.cid) for donationCampaign in DonationCampaignIpfsGateway.objects.all()]