import uuid

from commons.helper import get_created_user_detail_translator
from commons.solr_helper import (
    _unescape_values,
    __get_created_dt
)
def createopty_solr_request_translator(data):
    input_data = {}

    input_data["Login_s"] = data.get("login", "")
    input_data["AccountId_s"] = data.get("account_id", "")
    input_data["AccountName_s"] = data.get("account_name", "")
    input_data["OpportunityName_s"] = data.get("opty_name", "")
    input_data["EstimatedQuantity_s"] = data.get("estimated_quantity", "")
    input_data["SalesStage_s"] = data.get("sales_stage", "")
    input_data["Status_s"] = data.get("status", "")
    input_data["Model_s"] = data.get("model", "")
    input_data["ExpectedOrderDate_s"] = data.get("expcected_order_date", "")
    input_data["DeliveryDate_s"] = data.get("expcected_delivery_date", "")
    input_data["Comments_s"] = data.get("comments", "")
    input_data["Reason1_s"] = data.get("reason_1", "")
    input_data["CRMAvgUnits_s"] = data.get("average_unit", "")
    input_data["Quoted_s"] = data.get("quoted", "")
    input_data["Reason2_s"] = data.get("reason_2", "")
    input_data["Reason3_s"] = data.get("reason_comment", "")
    input_data["LastUpdated_dt"] = __get_created_dt()
    input_data["DealerCode_s"] = data.get("dealer_code", "")

    input_data["OptyId_s"] = str(uuid.uuid1())
    input_data["MarketingLeadId_s"] = data.get("marketing_lead_id", "")
    input_data["TurnInLeadId_s"] = data.get("turnin_lead_id", "")
    input_data["Attachment_ss"] = data.get("attachment", [])
    input_data["PositionId_s"] = data.get("position_id", [])
    input_data["SyncStatus_s"] = "False"

    input_data["Created_dt"] = __get_created_dt()

    created_user_data = get_created_user_detail_translator(data)
    input_data.update(created_user_data)

    return _unescape_values(input_data)

def update_opty_solr_request_translator(data, solr_obj):

    if data.get("opty_name"):
        solr_obj["OpportunityName_s"] = data.get("opty_name", "")

    if data.get("estimated_quantity"):
        solr_obj["EstimatedQuantity_s"] = data.get("estimated_quantity", "")

    if data.get("sales_stage"):
        solr_obj["SalesStage_s"] = data.get("sales_stage", "")

    if data.get("status"):
        solr_obj["Status_s"] = data.get("status", "")

    if data.get("model"):
        solr_obj["Model_s"] = data.get("model", "")

    if data.get("expcected_order_date"):
        solr_obj["ExpectedOrderDate_s"] = data.get("expcected_order_date", "")

    if data.get("expcected_delivery_date"):
        solr_obj["DeliveryDate_s"] = data.get("expcected_delivery_date", "")

    if data.get("comments"):
        solr_obj["Comments_s"] = data.get("comments", "")

    if data.get("reason_1"):
        solr_obj["Reason1_s"] = data.get("reason_1", "")

    if data.get("average_unit"):
        solr_obj["CRMAvgUnits_s"] = data.get("average_unit", "")

    if data.get("quoted"):
        solr_obj["Quoted_s"] = data.get("quoted", "")

    if data.get("reason_2"):
        solr_obj["Reason2_s"] = data.get("reason_2", "")

    if data.get("reason_comment"):
        solr_obj["Reason3_s"] = data.get("reason_comment", "")

    solr_obj["LastUpdated_dt"] = __get_created_dt()

    if data.get("account_name"):
        solr_obj["AccountName_s"] = data.get("account_name", "")

    if data.get("position_id"):
        solr_obj["PositionId_s"] = data.get("position_id", [])

    if data.get("attachment"):
        solr_obj["Attachment_ss"] = data.get("attachment", [])

    if data.get("user_details"):
        user_data = get_created_user_detail_translator(data)
        solr_obj.update(user_data)

    if data.get("siebel_opty_id"):
        solr_obj["SiebelOptyId_s"] = data.get("siebel_opty_id")

    if data.get("sync_status"):
        solr_obj["SyncStatus_s"] = data.get("sync_status")

    return solr_obj


