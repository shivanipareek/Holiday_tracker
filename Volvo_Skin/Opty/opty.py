from base import BaseClass


class Opty(BaseClass):
    def __init__(self, data):
        self.account_id = data.get("AccountId_s", "")
        self.account_name = data.get("AccountName_s", "")
        self.opty_name = data.get("OpportunityName_s", "")
        self.estimated_quantity = data.get("EstimatedQuantity_s", "")
        self.sales_stage = data.get("SalesStage_s", "")
        self.status = data.get("Status_s", "")
        self.model = data.get("Model_s", "")
        self.expcected_order_date = data.get("ExpectedOrderDate_s", "")
        self.expcected_delivery_date = data.get("DeliveryDate_s", "")
        self.comments = data.get("Comments_s", "")

        self.opty_id = data.get("OptyId_s", "")