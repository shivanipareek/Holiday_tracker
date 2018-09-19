
import json

from commons.position.models import position


def list_position_response_translator(core_response):

    if type(core_response) != list:
        core_json_object = core_response.json()
    else:
        core_json_object = core_response

    response_list = []

    for position_json in core_json_object:

        position_obj = position.Position(position_json)
        response_list.append(json.loads(position_obj.toJSON()))

    return response_list
