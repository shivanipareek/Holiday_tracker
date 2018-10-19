import competitor_siebel_xml
import requests
from requests.auth import HTTPBasicAuth
from siebel_request_translator import competitor_siebel_req_translator
STATIC_SIEBEL_URL = "https://wsp-qa.it.volvo.com/BOOMBOX/eai_anon_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute"

USER_NAME = "XW68319"

PASSWORD = "honest01"

# def siebel_req_translator(data):
#
#
#     final_tuple = (
#         data.get("Login_s", ""),
#         data.get("DealerCode_s", "Macasa"),
#         data.get("SiebelOptyId_s", ""),
#         data.get("SaleStage", ""),
#         data.get("PositionId_s", ""),
#         data.get("Make_s", "Renault"),
#         data.get("Name_s", ""),
#         data.get("EstQty_s", ""),
#         data.get("ComModel_s", ""),
#         data.get("CompetitorsPrice_s", ""),
#         data.get("SalesType_s", ""),
#         data.get("ComComments_s", ""),
#     )
#
#     return final_tuple


def create_competitor_in_siebel(data):
    competitor_tuple =  competitor_siebel_req_translator(data)

    competitor_header = competitor_siebel_xml.COMPETITOR_HEADER
    competitor_data = competitor_siebel_xml.COMPETITOR_DATA

    competitor_response = requests.post(url=STATIC_SIEBEL_URL,
                                        data=competitor_data,
                                        auth=HTTPBasicAuth(USER_NAME,PASSWORD),
                                        headers=competitor_header)
    print competitor_response.text
    # if competitor_response.status_code == 200:
    #   print "sucessfully updated to siebel"