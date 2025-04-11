from ..models import UserIpfsGateway
from helpers import IpfsHelper

class UserIpfsGatewayService:
    
    @staticmethod
    def saveUserIpfsRecord(walletAddress, cid):
        userIpfsGateway = UserIpfsGateway(walletAddress = walletAddress, cid = cid)
        userIpfsGateway.save()
        return True
    
    @staticmethod
    def deleteUserIpfsRecord(walletAddress: str):
        return UserIpfsGateway.objects.filter(walletAddress=walletAddress).delete()

    @staticmethod 
    def updateUserIpfsRecord(walletAddress: str, cid: str):
        userIpfsRecord = UserIpfsGateway.objects.get(walletAddress=walletAddress)
        userIpfsRecord.cid = cid
        userIpfsRecord.save()
        return True

    @staticmethod
    def getUserIpfsData(walletAddress):
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
    
    @staticmethod
    def getAllUserIpfsData():
        return [IpfsHelper.fetchData(userIpfsRecord.cid) for userIpfsRecord in UserIpfsGateway.objects.all()]

        