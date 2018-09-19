from base import BaseClass


class Position(BaseClass):
    def __init__(self, data):
        self.first_name = data.get("PostnPREmpFstName_s", "")
        self.last_name = data.get("PostnPREmpLastName_s", "")
        self.primary_position_id = data.get("PrPostnID_s", "")
        self.position_id = data.get("PostnID_s", "")
        self.login = data.get("Login_s", "")
        self.created = data.get("Created_dt", "")
        self.cell_number = data.get("PostnPREmpCellphNnum_s", "")
        self.position_type = data.get("PostnType_s", "")
        self.account = data.get("AccountId_ss", "")
        self.parent_pos_id = data.get("Parent_Position_Id_s","")
