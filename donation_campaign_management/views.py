from rest_framework.decorators import api_view
from django.http import JsonResponse
from .controllers import DonationCampaignController
from helpers import RequestHelper

# Create your views here.

donationCampaignController = DonationCampaignController()

@api_view(["POST"])
def createDonationCampaign(request, walletAddress):
    return JsonResponse(donationCampaignController.createDonationCampaign(RequestHelper.getRequestBody(request)))

@api_view(["GET"])
def getAllDonationCampaigns(request):
    return JsonResponse(donationCampaignController.getDonationCampaigns(), safe=False)


@api_view(["GET", "PATCH", "DELETE"])
def handleDonationCampaignRequest(request, walletAddress, id):
    if request.method == "GET":
        return JsonResponse(donationCampaignController.getDonationCampaign(id))
    elif request.method == "PATCH":
        return JsonResponse(donationCampaignController.updateDonationCampaign(RequestHelper.getRequestBody(request), id))
    elif request.method == "DELETE":
        return JsonResponse(donationCampaignController.deleteDonationCampaign(id), safe=False)


@api_view(["GET"])
def getDonationCampaign(request, id):
    return JsonResponse(donationCampaignController.getDonationCampaign(id))