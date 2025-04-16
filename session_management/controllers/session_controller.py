from ..services import SessionService
from decorators import singleton

@singleton
class SessionController:

    def __init__(
        self,
        sessionService = SessionService()
    ):
        self.sessionService = sessionService

    def addSession(self, walletAddress: str, signature: str):
        return self.sessionService.addSession(walletAddress, signature)
    
    def removeSession(self, sessionToken: str):
        return self.sessionService.removeSession(sessionToken)