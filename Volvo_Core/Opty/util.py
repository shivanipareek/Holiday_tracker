
import requests

def get_opty_from_solr(url, opty_id=None):
    opty_data = False
    opty_detail_url = url

    if opty_id:
        opty_detail_url = opty_detail_url % opty_id

    opty_detail_url = "http://54.200.153.229:8983/solr/" + opty_detail_url

    opty_response = requests.get(opty_detail_url)

    if opty_response.status_code == 200:
        opty_data = opty_response.json()
        opty_data = opty_data.get('response', {}).get('docs', [])
    return opty_data

