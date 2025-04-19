from session_management.models import Session

class RemoveSessionCommand:

    def __init__(self, sessionToken):
        self.sessionToken = sessionToken

    def execute(self):
        Session.objects.filter(sessionToken=self.sessionToken).delete()
        return {
            "code": 200,
            "message": "logged out"
        }
