from ..services import UserIpfsGatewayService
from decorators import singleton


@singleton
class UserIpfsGatewayController:

    def __init__(
        self,
        userIpfsGatewayService = UserIpfsGatewayService()
    ):
        self.userIpfsGatewayService = userIpfsGatewayService
    
    def saveUserIpfsRecord(self, walletAddress: str, cid: str):
        return self.userIpfsGatewayService.saveUserIpfsRecord(walletAddress, cid)
    
    def deleteUserIpfsRecord(self, walletAddress: str):
        return self.userIpfsGatewayService.deleteUserIpfsRecord(walletAddress)
     
    def updateUserIpfsRecord(self, walletAddress: str, cid: str):
        return self.userIpfsGatewayService.updateUserIpfsRecord(walletAddress, cid)

    def getUserIpfsData(self, walletAddress: str):
        return self.userIpfsGatewayService.getUserIpfsData(walletAddress)
    
    def getAllUserIpfsData(self):
        return self.userIpfsGatewayService.getAllUserIpfsData()