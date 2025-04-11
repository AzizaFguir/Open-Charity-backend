from session_management.models import Session
from helpers import StringHelper
from ipfs_gateway.controllers import UserIpfsGatewayController


class SessionService: 

    @staticmethod
    def addSession(walletAddress: str, signature: str): 
        try:
            userIpfsRecord = UserIpfsGatewayController.getUserIpfsData(walletAddress)

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

    
    @staticmethod
    def removeSession(sessionToken: str):
        Session.objects.filter(sessionToken=sessionToken).delete()

        return {
            "code": 200,
            "message": "logged out",
        }
        
        