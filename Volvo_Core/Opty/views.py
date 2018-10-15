# Create your views here.
import requests
from rest_framework.response import Response
from Volvo_Core.Static_Solr_url import OPTY_DATA_URL
from rest_framework.views import APIView
from rest_framework import status
import logging
import json
from Commons.conf import SOLR_BASE_URL
from Opty.System_error import *

logger =logging.getLogger("opty_logs")

class OptyDetails(APIView):

    def post(self,request, *args, **kwargs):
        data = request.data
        position_id = data.get("position_id")
        #Error Check
        error_status = check_search_opty_errors(data)
        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED
                            )
        logger.info("Input Data")
        logger.info(json.dumps(data))
        opty_search_url = OPTY_DATA_URL
        opty_search_url =  SOLR_BASE_URL + opty_search_url % position_id
        opty_response = requests.get(opty_search_url)
        if opty_response.status_code == 200:
            opty_data = opty_response.json()
            opty_data = opty_data.get('response', {}).get('docs', [])
        return Response(opty_data)

