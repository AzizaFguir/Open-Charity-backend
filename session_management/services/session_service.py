from session_management.models import Session
from helpers import StringHelper
from ipfs_gateway.controllers import UserIpfsGatewayController


class SessionService: 

    def __init__(
        self,
        userIpfsGatewayController = UserIpfsGatewayController()
    ):
        self.userIpfsGatewayController = userIpfsGatewayController

    def addSession(self, walletAddress: str, signature: str): 
        try:
            userIpfsRecord = self.userIpfsGatewayController.getUserIpfsData(walletAddress)

            if userIpfsRecord["walletAddress"] == "":
                return {
                    "code": 404,
                    "message": "user not found"
                }
            
            else:
                session = Session(walletAddress = walletAddress, sessionToken=signature)
                session.save()
                return {
                    "code": 200,
                    "message": "connected",
                    "sessionToken": session.sessionToken
                }
        
        except KeyError:
           return {
                "code": 401,
                "message": "authentication failed"
            }

    
    def removeSession(self, sessionToken: str):
        Session.objects.filter(sessionToken=sessionToken).delete()

        return {
            "code": 200,
            "message": "logged out",
        }
        
        