import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.parsers import XMLParser
from commons import conf
from dealer.siebel_request_translator import (
    create_dealer_request_translator,
    update_dealer_translator
)
from dealer.utils import (
    get_dealer_data,
    add_dealer_to_solr
)
from commons.parser import XMLRenderer
from dealer import dealer_siebel_xml
from commons.helper import (
    soap_keys_translator,
    wsdl_authentication,
    auth_soap_keys_translator
)

logger = logging.getLogger("dealer")

class DealerSyncView(APIView):
    """
    Dealer Sync From Siebel
    """
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)

    def post(self, request, *args, **kwargs):

        dealer_url = "api/sync/dealer/}"

        prefix_variable = "{" + conf.SIEBEL_BASE_URL + dealer_url
        data = request.data

        header_data          = data.get("{http://schemas.xmlsoap.org/soap/envelope/}Header")
        auth                 = header_data.get("{"+ conf.SIEBEL_BASE_URL + dealer_url +"Authentication")
        translated_auth_data = auth_soap_keys_translator(prefix_variable,auth)
        is_authentication    = wsdl_authentication(translated_auth_data)
        response_xml = dealer_siebel_xml.DEALER_RESPONSE_XML

        if is_authentication:
            return Response(response_xml % ("","",is_authentication.get("error_msg")))

        body_data  = data.get("{http://schemas.xmlsoap.org/soap/envelope/}Body")
        input_data = body_data.get("{"+ conf.SIEBEL_BASE_URL + dealer_url + "AudetemiDealerReq")
        req_data   = input_data.get("{" + conf.SIEBEL_BASE_URL + dealer_url + "DealerData")

        translated_dealer_data = soap_keys_translator(prefix_variable,req_data)


        dealer_id = translated_dealer_data.get("DealerId")

        if dealer_id:

            check_dealer_data = get_dealer_data(dealer_id)

            if check_dealer_data:
                dealer_solr_data = update_dealer_translator(translated_dealer_data, check_dealer_data[0])
            else:
                dealer_solr_data = create_dealer_request_translator(translated_dealer_data)

            dealer_data = add_dealer_to_solr(dealer_solr_data)

            response_xml = dealer_siebel_xml.DEALER_RESPONSE_XML

            if dealer_data:
                response_data = response_xml % ("", "200", "Dealer data successfully updated")
            else:
                response_data = response_xml % ("", "400", "Failed to Update")

            return Response(response_data)

