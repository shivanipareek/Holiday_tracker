import json
import xmltodict

from opty.siebel_mapper import OptyResponseMapper

def convert_xml_to_flat_dict(data, value_dict = {}):
    for key, value in data.iteritems():
        if isinstance(value, dict):
            convert_xml_to_flat_dict(value, value_dict)
    else:
        value_dict.update({key : value})
    return value_dict

def sieble_opty_response_translator(response_data):

    core_response = xmltodict.parse(response_data)
    core_response = json.loads(json.dumps(core_response))
    opty_json = convert_xml_to_flat_dict(core_response)
    opty_data = opty_json.get("ns:Receive_spcOpportunity_Output")
    opty_obj = OptyResponseMapper(opty_data)
    response_data = json.loads(opty_obj.toJSON())

    return response_data


