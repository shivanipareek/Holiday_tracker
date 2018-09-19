import json
from cv360.mobile.account.models import account

def acc_response_translator(core_response):

    if type(core_response) != list:
        core_json_object = core_response.json()
    else:
        core_json_object = core_response

    response_list = []
    for account_json in core_json_object:
        acc_obj = account.AccList(account_json)
        response_data = json.loads(acc_obj.toJSON())
        response_list.append(response_data)
    return response_list