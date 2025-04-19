from abc import ABC


class IUserIpfsGatewayController(ABC):

    def saveUserIpfsRecord(self, walletAddress: str, cid: str): pass
    
    def deleteUserIpfsRecord(self, walletAddress: str): pass
     
    def updateUserIpfsRecord(self, walletAddress: str, cid: str): pass

    def getUserIpfsData(self, walletAddress: str): pass
    
    def getAllUserIpfsData(self): pass