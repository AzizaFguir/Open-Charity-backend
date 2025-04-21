from datetime import datetime
import core.models.Donation as Donation

class DonationCampaign: 

    def __init__(self, id, title, description, wallpaper, beneficiary, donations: dict={}, openStatus=True,dateCreated=None):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__wallpaper = wallpaper
        self.__beneficiary = beneficiary
        self.__donations: dict = donations
        self.__openStatus = openStatus
        if isinstance(dateCreated, str):
            # If the string is in ISO format, convert to datetime
            self.__dateCreated = datetime.fromisoformat(dateCreated)
        else:
            self.__dateCreated = dateCreated if dateCreated else datetime.now()

    def getId(self):
        return self.__id
    
    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description
    
    def getWallpaper(self):
        return self.__wallpaper
    
    def getBeneficiary(self):
        return self.__beneficiary
    
    def getDonations(self):
        return self.__donations
    
    def getOpenStatus(self):
        return self.__openStatus

    def getDateCreated(self):
        # Ensure __dateCreated is always a datetime object before calling isoformat
        if isinstance(self.__dateCreated, str):
            self.__dateCreated = datetime.fromisoformat(self.__dateCreated)
        return self.__dateCreated.isoformat()

    def getData(self):
        return {
            "id": self.getId(),
            "title": self.getTitle(),
            "description": self.getDescription(),
            "beneficiary": self.getBeneficiary(),
            "wallpaper": self.getWallpaper(),
            "donations": self.getDonations(),
            "openStatus": self.getOpenStatus(),
            "dateCreated": self.getDateCreated()
        }
    

    def setTitle(self, title: str):
        self.__title = title
    
    def setDescription(self, description: str):
        self.__description = description
    
    def setId(self, id: str):
        self.__id = id
    
    def setOpenStatus(self, openStatus: bool):
        self.__openStatus = openStatus
    
    def setWallpaper(self, wallpaper: str):
        self.__wallpaper = wallpaper
    
    def addDonation(self, donation: Donation):
        self.__donations[donation.getId()] = donation.getData()

    def update(self, title: str = None, description: str = None, openStatus: bool = None, wallpaper: str = None):
        if title is not None:
            self.setTitle(title)
        if description is not None:
            self.setDescription(description)
        if openStatus is not None:
            self.setOpenStatus(openStatus)    
        if wallpaper is not None:
            self.setWallpaper(wallpaper)
