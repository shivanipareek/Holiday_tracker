from siebel_request_translator import opty_siebel_req_translator
import opty_siebel_xml
import requests
from requests.auth import HTTPBasicAuth
STATIC_SIEBEL_URL = "https://wsp-qa.it.volvo.com/BOOMBOX/eai_anon_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute"

USER_NAME = "XW68319"

PASSWORD = "honest01"




def create_opty_in_siebel(data):
    opty_tuple =  opty_siebel_req_translator(data)

    opty_header = opty_siebel_xml.OPTY_HEADER
    opty_data = opty_siebel_xml.OPTY_DATA

    opty_response = requests.post(url=STATIC_SIEBEL_URL,
                                        data=opty_data,
                                        auth=HTTPBasicAuth(USER_NAME,PASSWORD),
                                        headers=opty_header)
    print opty_response.text