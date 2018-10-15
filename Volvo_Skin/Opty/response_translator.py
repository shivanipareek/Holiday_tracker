import json

from Opty.opty import Opty

def opty_response_translator(core_response, user=None):

    if type(core_response) != list:
        core_json_object = core_response.json()
        if type(core_json_object) != list and core_json_object.get(
                "opty_details"):
            core_json_object = [core_json_object.get("opty_details")]
    else:
        core_json_object = core_response

    response_list = []

    for opty_json in core_json_object:
        opty_obj = Opty(opty_json)
        response_data = json.loads(opty_obj.toJSON())
        response_list.append(
            response_data
        )
    return response_list
