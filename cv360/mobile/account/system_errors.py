from commons import error_conf

def check_for_acc_by_pos_input_errors(pos_id):
    '''
       Error Handling For opty by position id
       '''
    if not pos_id.get("pos_id"):
        return error_conf.POS_ID_NOT_PROVIDED

    return False
