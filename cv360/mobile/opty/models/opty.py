from base import BaseClass


class CreateOpty(BaseClass):

    def __init__(self, data):
        self.account_id = data.get("AccountId_s", "")
        self.account_name = data.get("AccountName_s", "")
        self.opty_name = data.get("OpportunityName_s", "")
        self.sales_stage = data.get("SalesStage_s", "")
        self.status = data.get("Status_s", "")
        self.model = data.get("Model_s", "")
        self.opty_id = data.get("OptyId_s", "")
        self.reason = data.get("Reason_s", "")
        self.quoted = data.get("Quoted_s", "")
        self.position_id = data.get("PositionId_s", "")
        self.created_date = data.get("Created_dt", "")
        self.updated_date = data.get("Updated_dt", "")

