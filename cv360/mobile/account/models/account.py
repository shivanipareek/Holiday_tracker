from base import BaseClass

class AccList(BaseClass):

    def __init__(self, data):
        self.account_id = data.get("AccountId_s", "")
        self.account_name = data.get("Name_s", "")
        self.Latitude = data.get("Latitude_s", "")
        self.Longitude = data.get("Longitude_s", "")


