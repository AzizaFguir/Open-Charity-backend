class LogoutUserCommand:

    def __init__(self, data, sessionController):
        self.sessionToken = data["sessionToken"]
        self.sessionController = sessionController

    def execute(self):
        return self.sessionController.removeSession(self.sessionToken)
