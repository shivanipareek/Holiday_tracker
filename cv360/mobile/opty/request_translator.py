
from commons.user_auth.helper import user_details_request_translator, get_user_login

def createopty_req_translator(data, user):
    input_data = {}
    position_id = data.get("position_id")[0]

    if data:
        input_data["login"] = get_user_login(user)
        input_data["account_id"] = data.get("account_id", "")
        input_data["account_name"] = data.get("account_name", "")
        input_data["opty_name"] = data.get("opty_name", "")
        input_data["sales_stage"] = data.get("sales_stage", "")
        input_data["status"] =data.get("status", "")
        input_data["reason"] = data.get("reason", "")
        input_data["quoted"] = data.get("quoted", "")
        input_data["reason_comment"] = data.get("reason_comment", "")
        input_data["position_id"] = data.get("position_id", [])
        input_data["attachment"] = data.get("attachment", [])
        input_data["user_details"] = user_details_request_translator(position_id, user)

    return input_data