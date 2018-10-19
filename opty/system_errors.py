
from VolvoCore import system_messages



def check_opty_by_pos_errors(data):

    if not data.get("pos_id"):
        return system_messages.POSITION_ID_NOT_PROVIDED

    return False

def check_create_opty_errors(data):

    if not data.get("login"):
        return system_messages.LOGIN_NOT_PROVIDED

    if not data.get("account_id"):
        return system_messages.ACCOUNT_NOT_PROVIDED

    if not data.get("opty_name"):
        return system_messages.OPTY_NAME_NOT_PROVIDED

    if not data.get("sales_stage"):
        return system_messages.SALES_STAGE_NOT_PROVIDED

    if not data.get("position_id"):
        return system_messages.POSITION_ID_NOT_PROVIDED

    return False

