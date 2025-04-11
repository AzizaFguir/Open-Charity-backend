import json

class RequestHelper: 

    @staticmethod
    def getRequestBody(request):
        return json.loads(request.body.decode("utf-8"))