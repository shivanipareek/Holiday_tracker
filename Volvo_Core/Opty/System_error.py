from Volvo_Core import System_message

def check_search_opty_errors(data):
    if not data.get("position_id"):
        return System_message.POSITION_ID_NOT_PROVIDED

    return False