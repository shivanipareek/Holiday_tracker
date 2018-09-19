from commons import error_conf

def check_for_opty_by_pos_input_errors(pos_id):

    if not pos_id.get("pos_id"):
        return error_conf.POS_ID_NOT_PROVIDED

    return False

def check_for_create_opty_errors(data):

    if not data:
        return error_conf.DATA_NOT_PROVIDED

    if not data.get("account_id"):
        return error_conf.ACCOUNT_ID_NOT_PROVIDED

    if not data.get("opty_name"):
        return error_conf.OPTY_NAME_NOT_PROVIDED

    if not data.get("position_id"):
        return error_conf.POSITION_ID_NOT_PROVIDED

    if data.get("sales_stage").lower()=="warranty register" and \
            data.get("status").lower()=="quoted" and \
            data.get("reason","")=="":

        return error_conf.REASON_1_NOT_PROVIDED