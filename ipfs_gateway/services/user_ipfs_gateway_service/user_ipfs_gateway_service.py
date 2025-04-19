from ipfs_gateway.models import UserIpfsGateway
from helpers import IpfsHelper
from decorators import singleton

@singleton
class UserIpfsGatewayService:
    
    def saveUserIpfsRecord(self, walletAddress, cid):
        userIpfsGateway = UserIpfsGateway(walletAddress = walletAddress, cid = cid)
        userIpfsGateway.save()
        return True
    
    def deleteUserIpfsRecord(self, walletAddress: str):
        return UserIpfsGateway.objects.filter(walletAddress=walletAddress).delete()

    def updateUserIpfsRecord(self, walletAddress: str, cid: str):
        userIpfsRecord = UserIpfsGateway.objects.get(walletAddress=walletAddress)
        userIpfsRecord.cid = cid
        userIpfsRecord.save()
        return True

    def getUserIpfsData(self, walletAddress):
        try:
            return IpfsHelper.fetchData(UserIpfsGateway.objects.get(walletAddress = walletAddress).cid)
        except UserIpfsGateway.DoesNotExist:
            return {
                "walletAddress": "",
                "username": "",
                "profilePic": "",
                "donations": {},
                "donationCampaigns": {}
            }
    
    def getAllUserIpfsData(self):
        return [IpfsHelper.fetchData(userIpfsRecord.cid) for userIpfsRecord in UserIpfsGateway.objects.all()]

        