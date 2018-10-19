import logging
import requests
from commons.conf import USER_NAME,PASSWORD
from requests.auth import HTTPBasicAuth
from opty.siebel_request_translator import __to_tuple_for_create_opty
import opty_siebel_xml
from models import Opty
from helper import update_opty_data_on_solr
from commons.conf import SIEBEL_HEADER
from siebel_response_translator import sieble_opty_response_translator

logger = logging.getLogger("opty")

def create_opty_in_siebel(data):



    if data.get("CRMAvgUnits_s") == "0":
        data["CRMAvgUnits_s"] = ""

    opty_data = __to_tuple_for_create_opty(data)
    opty_header = opty_siebel_xml.CREATE_OPTY_HEADER
    opty_url = opty_siebel_xml.CREATE_OPTY_URL
    opty_data = opty_siebel_xml.CREATE_OPTY_DATA % opty_data
    print "opty_data",opty_data

    opty_response = ""
    logger.info("........Siebel Opty Data.........")
    logger.info(opty_data)
    get_opty_response = requests.post(opty_url,
                                      auth=HTTPBasicAuth(USER_NAME, PASSWORD),
                                      data=opty_data,
                                      headers=opty_header)

    logger.info("..........Opty Siebel Response.......")
    logger.info(get_opty_response.text)

    if get_opty_response.status_code == 200:
        opty_response = sieble_opty_response_translator(get_opty_response.text)
        solr_opty_id = data.get("OptyId_s")
        opty_siebel_id = opty_response.get("SiebelOptyId_s")

        if opty_siebel_id:
            create_opty_data = Opty.objects.get_or_create(
                opty_id=solr_opty_id
            )
            if create_opty_data:
                create_opty_data[0].seibel_opty_id = opty_siebel_id
                create_opty_data[0].save()

            updated_solr_dict = {
                "sync_status": True,
                "siebel_opty_id": opty_siebel_id
            }

            update_opty_data_on_solr(updated_solr_dict, solr_opty_id)

    return opty_response




