from siebel_request_translator import contact_siebel_req_translator
import contact_siebel_xml
import requests
from requests.auth import HTTPBasicAuth
STATIC_SIEBEL_URL = "https://wsp-qa.it.volvo.com/BOOMBOX/eai_anon_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute"

USER_NAME = "XW68319"

PASSWORD = "honest01"

def create_contact_in_siebel(data):
    contact_tuple =  contact_siebel_req_translator(data)

    contact_header = contact_siebel_xml.CONTACT_DATA
    contact_data = contact_siebel_xml.CONTACT_DATA

    contact_response = requests.post(url=STATIC_SIEBEL_URL,
                                        data=contact_data,
                                        auth=HTTPBasicAuth(USER_NAME,PASSWORD),
                                        headers=contact_header)
    print contact_response.text