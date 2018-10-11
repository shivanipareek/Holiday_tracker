from Commons import error_conf

def check_for_postion_search(data):
    position_id = data.get("position_id")
    if not position_id:
        return error_conf.POSITION_ID_NOT_PROVIDED
