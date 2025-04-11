from ..services import DonationService

class DonationController:
    
    @staticmethod
    def addDonation(donationData: dict):
        return DonationService.addDonation(donationData)
    
