from ..services import UserIpfsGatewayService

class UserIpfsGatewayController:
    
    @staticmethod
    def saveUserIpfsRecord(walletAddress: str, cid: str):
        return UserIpfsGatewayService.saveUserIpfsRecord(walletAddress, cid)
    
    @staticmethod
    def deleteUserIpfsRecord(walletAddress: str):
        return UserIpfsGatewayService.deleteUserIpfsRecord(walletAddress)
    
    @staticmethod 
    def updateUserIpfsRecord(walletAddress: str, cid: str):
        return UserIpfsGatewayService.updateUserIpfsRecord(walletAddress, cid)

    @staticmethod
    def getUserIpfsData(walletAddress: str):
        return UserIpfsGatewayService.getUserIpfsData(walletAddress)
    
    def getAllUserIpfsData():
        return UserIpfsGatewayService.getAllUserIpfsData()