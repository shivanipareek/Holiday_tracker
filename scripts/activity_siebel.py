from siebel_request_translator import activity_siebel_req_translator
import activity_siebel_xml
import requests
from requests.auth import HTTPBasicAuth
STATIC_SIEBEL_URL = "https://wsp-qa.it.volvo.com/BOOMBOX/eai_anon_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute"

USER_NAME = "XW68319"

PASSWORD = "honest01"

def create_activity_in_siebel(data):
    activity_tuple =  activity_siebel_req_translator(data)

    activity_header = activity_siebel_xml.CREATE_ACTIVITY_HEADER
    activity_data = activity_siebel_xml.ACTIVITY_CREATE_DATA

    activity_response = requests.post(url=STATIC_SIEBEL_URL,
                                        data=activity_data,
                                        auth=HTTPBasicAuth(USER_NAME,PASSWORD),
                                        headers=activity_header)
    print activity_response.text

