from session_management.commands.add_session_command import AddSessionCommand
from session_management.commands.remove_session_command import RemoveSessionCommand
from ipfs_gateway.controllers import UserIpfsGatewayController

class SessionService:

    def __init__(self, userIpfsGatewayController=UserIpfsGatewayController()):
        self.userIpfsGatewayController = userIpfsGatewayController

    def addSession(self, walletAddress: str, signature: str):
        return AddSessionCommand(walletAddress, signature, self.userIpfsGatewayController).execute()

    def removeSession(self, sessionToken: str):
        return RemoveSessionCommand(sessionToken).execute()
