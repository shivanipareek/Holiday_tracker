from django.shortcuts import render

# Create your views here.
import json
import requests
from rest_framework.response import Response
from rest_framework.views import (
    APIView
)
from rest_framework import status
from Commons.conf import *
from response_translator import opty_response_translator
from Volvo_Skin import System_error
import logging
from Commons import error_conf

logger = logging.getLogger('opty_s')

class OptySearchDetails(APIView):
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logging.info("Search Opty from Position ID")
        data = request.data
        logging.info("Postion_id" + json.dumps(data))

        data["position_id"] = data.get("position_id")

        opty_data = data
        error_check = System_error.check_for_postion_search(opty_data)
        if not error_check:
            opty_details_url = Base_url + 'api/opty'
            search_opty_response = requests.post(
                url=opty_details_url,
                data=json.dumps(opty_data),
                headers={"Content-Type": "application/json"})

            if search_opty_response.status_code ==200:
                opty_json_response = opty_response_translator(
                    search_opty_response,
                    request.user)
                return Response(opty_json_response)
                logger.info("Opty data fetched")
            elif search_opty_response.status_code ==412:
                logger.info(
                    "Error response :" + json.dumps(search_opty_response.json()))
                return Response(
                    {'msg': search_opty_response.json().get("error_msg", "")},
                    status=status.HTTP_412_PRECONDITION_FAILED)

            logger.info("Error response :" + json.dumps(search_opty_response.json()))
            return Response(error_conf.PROBLEM_WITH_CORE,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        return Response(error_check,
                        status=status.HTTP_412_PRECONDITION_FAILED)




