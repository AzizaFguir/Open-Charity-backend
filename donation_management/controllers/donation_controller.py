from ..services import DonationService
from common import singleton


@singleton
class DonationController:

    def __init__(self, donationService = DonationService()):
        self.donationService = donationService
    
    def addDonation(self, donationData: dict):
        return self.donationService.addDonation(donationData)
    
