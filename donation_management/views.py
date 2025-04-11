from rest_framework.decorators import api_view
from django.http import JsonResponse
from .controllers import DonationController
from helpers import RequestHelper

# Create your views here.

@api_view(["POST"])
def addDonation(request, walletAddress, id):
    return JsonResponse(DonationController.addDonation(RequestHelper.getRequestBody(request)))
