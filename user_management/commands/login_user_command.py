class LoginUserCommand:

    def __init__(self, data, sessionController):
        self.walletAddress = data["walletAddress"]
        self.signature = data["signature"]
        self.sessionController = sessionController

    def execute(self):
        return self.sessionController.addSession(self.walletAddress, self.signature)
