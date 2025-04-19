from abc import ABC

class IUserIpfsGatewayService(ABC):
    
    def saveUserIpfsRecord(self, walletAddress, cid): pass 
    
    def deleteUserIpfsRecord(self, walletAddress: str): pass

    def updateUserIpfsRecord(self, walletAddress: str, cid: str): pass

    def getUserIpfsData(self, walletAddress): pass
    
    def getAllUserIpfsData(self): pass