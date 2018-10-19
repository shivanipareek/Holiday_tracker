import json
import requests

from commons.conf import SOLR_BASE_URL



def create_or_update_opty(opty_data):
    opty_url = ""

    opty_header = {'content-type': 'text/xml',
                   'SOAPAction': '"document/http://siebel.com/asi/:SFATMCVContactInsertOrUpdate"'}

    opty_response = requests.post(url=opty_url,
                                  data=opty_data,
                                  headers=opty_header)
    return opty_response


def get_opty_from_solr(url, opty_id=None):
    opty_data = False
    opty_detail_url = url

    if opty_id:
        opty_detail_url = opty_detail_url % opty_id

    opty_detail_url = SOLR_BASE_URL + opty_detail_url

    opty_response = requests.get(opty_detail_url)

    if opty_response.status_code == 200:
        opty_data = opty_response.json()
        opty_data = opty_data.get('response', {}).get('docs', [])
    return opty_data


def _list_to_solr_filter(data):
    data_list = json.dumps(data)
    data_list = data_list.replace("[", "(")
    data_list = data_list.replace("]", ")")
    data_list = data_list.replace(", ",",")
    return data_list

def _list_space_to_solr_filter(data):
    # data_list = json.dumps(data)
    # data_list = data_list.replace("[", "(")
    # data_list = data_list.replace("]", ")")
    # data_list = data_list.replace(", "," ")
    data_list = '('+ ' '.join(data) +')'
    return data_list
