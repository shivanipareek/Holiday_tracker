from VolvoCore import system_messages

def check_acc_by_pos_errors(data):

    if not data.get("pos_id"):
        return system_messages.POSITION_ID_NOT_PROVIDED

    return False
