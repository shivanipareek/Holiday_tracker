import logging

import requests
from requests import ConnectionError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from VolvoCore import static_solr_urls
from VolvoCore import system_messages
from commons import conf
from opty import solr_request_translator as srt
from opty import solr_utility
from opty.siebel_utility import create_opty_in_siebel
from opty.system_errors import (

    check_create_opty_errors,
    check_opty_by_pos_errors,
)

logger = logging.getLogger("opty")


class CreateOptyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        error_status = check_create_opty_errors(data)

        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        createopty_solr_data = srt.createopty_solr_request_translator(data)

        if solr_utility.addopty_solr(createopty_solr_data):

            create_opty_in_siebel(createopty_solr_data)

            return Response({'msg': "Opty Created Successfully",
                             "opty_details": createopty_solr_data},
                            status=status.HTTP_201_CREATED)

        logger.info("Failed to push data to solr!")
        return Response({'msg': system_messages.CREATE_OPTY_FAILED_RESPONSE},
                        status=status.HTTP_412_PRECONDITION_FAILED)


class GetOptyByPosAPIView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        pos_id = data.get("pos_id")
        pos_id = "(" + " ".join(pos_id) + ")"

        error_status = check_opty_by_pos_errors(data)

        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        get_opty_by_pos = static_solr_urls.GET_OPTY_BY_POS

        get_opty_by_pos = conf.SOLR_BASE_URL + get_opty_by_pos % pos_id

        try:
            response_data = requests.get(get_opty_by_pos)


        except ConnectionError as ce:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        if response_data.status_code == 200:
            response_data_json = response_data.json()
            response_data = response_data_json.get("response", {}).get("docs", [])

            return Response({"Msg": "Successfully fetched Opty details by Position ID", "result": response_data})

        return Response({"msg": "Failed to fetched Opty Details"})


