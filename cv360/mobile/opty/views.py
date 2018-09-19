# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import json
import logging
import requests
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from requests import ConnectionError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import (APIView)
import request_translator as rqt
import response_translator as rst
from commons import (
    BASE_URL,
    WriteJSONParser,
    error_conf,
)
from . import system_errors

logger = logging.getLogger('opty')

class Createopty(APIView):

    parser_classes = [WriteJSONParser]
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        data = request.data
        error_status = system_errors.check_for_create_opty_errors(data)

        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        input_data = rqt.createopty_req_translator(data, request.user)

        create_opty_url = BASE_URL + "api/createopty/"

        try:
            response_data = requests.post(url=create_opty_url,
                                          data=json.dumps(input_data),
                                          headers={
                                              "Content-Type": "application/json"})
        except ConnectionError as ce:
            return Response(error_conf.UNABLE_TO_REACH_CORE,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        if response_data.status_code == 201:
            createopty_json_response = rst.createopty_response_translator(response_data)
            return Response({"msg":"Opty Created Successfully","Result":createopty_json_response})

        return Response("Failed to create opty")



class GetOptyByPosition(APIView):

    parser_classes = [WriteJSONParser]
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        pos_id = request.data.get("pos_id",[])
        pos_id = {"pos_id":pos_id}
        error_checks = system_errors.check_for_opty_by_pos_input_errors(pos_id)

        if error_checks:
            return Response(error_checks,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        get_opty_by_pos = BASE_URL + "api/opty/by_pos/"

        try:
            response_data = requests.post(url=get_opty_by_pos,
                                         data=json.dumps(pos_id),
                                         headers={
                                             "Content-Type": "application/json"})
        except ConnectionError as ce:
            return Response(error_conf.UNABLE_TO_REACH_CORE,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        if response_data.status_code == 200:
            return Response(response_data.json())

        return Response({"msg":"Failed"})

