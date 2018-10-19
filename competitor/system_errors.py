
from VolvoCore import system_messages

def  check_opty_and_pos_errors(data):

    if not data.get("position_id"):
        return system_messages.POSITION_ID_NOT_PROVIDED
    # if not data.get("opty_id"):
    #     return system_messages.OPTY_ID_NOT_PROVIDED

    return False