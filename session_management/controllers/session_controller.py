from ..services import SessionService

class SessionController:

    @staticmethod
    def addSession(walletAddress: str, signature: str):
        return SessionService.addSession(walletAddress, signature)
    
    @staticmethod
    def removeSession(sessionToken: str):
        return SessionService.removeSession(sessionToken)