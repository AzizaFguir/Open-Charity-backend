from session_management.models import Session
from helpers import StringHelper
from ipfs_gateway.controllers import UserIpfsGatewayController

class AddSessionCommand:

    def __init__(self, walletAddress, signature, userIpfsGatewayController=None):
        self.walletAddress = walletAddress
        self.signature = signature
        self.userIpfsGatewayController = userIpfsGatewayController or UserIpfsGatewayController()

    def execute(self):
        try:
            userIpfsRecord = self.userIpfsGatewayController.getUserIpfsData(self.walletAddress)

            if userIpfsRecord["walletAddress"] == "":
                return {
                    "code": 404,
                    "message": "user not found"
                }

            session = Session(walletAddress=self.walletAddress, sessionToken=self.signature)
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
