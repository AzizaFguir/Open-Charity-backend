from ...services import DonationService
from decorators import singleton
from .i_donation_controller import IDonationController


@singleton
class DonationController(IDonationController):

    def __init__(self, donationService = DonationService()):
        self.donationService = donationService
    
    def addDonation(self, donationData: dict):
        return self.donationService.addDonation(donationData)
    
