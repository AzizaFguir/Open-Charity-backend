import core.models.User as User
from datetime import date

class Donation:

    def __init__(self, id, donor: User, donationCampaignId: str, amount: int, recipient_wallet_address: str):
        self.__id = id
        self.__amount = amount
        self.__dateDonated = date.today()
        self.__donationCampaign = donationCampaignId
        self.__donor = donor
        self.__recipient_wallet_address = recipient_wallet_address
        
        # Apply the OCL NoSelfDonation constraint
        self.__check_no_self_donation()

    def __check_no_self_donation(self):
        # Ensure donor and recipient are not the same
        if self.__donor.getWalletAddress() == self.__recipient_wallet_address:
            raise ValueError("A user cannot donate to themselves.")

    def getId(self):
        return self.__id

    def getAmount(self):
        return self.__amount
    
    def getDateDonated(self):
        return self.__dateDonated.isoformat()
    
    def getDonationCampaign(self):
        return self.__donationCampaign
    
    def getDonor(self):
        return self.__donor
    
    def getRecipient(self):
        return self.__recipient_wallet_address

    def getData(self):
        return {
            "amount": self.getAmount(),
            "dateDonated": self.getDateDonated(),
            "donationCampaignId": self.getDonationCampaign(),
            "donor": self.getDonor().getWalletAddress(),
            "recipient": self.getRecipient()
        }
