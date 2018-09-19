import requests
import json
import logging

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from commons.position import response_translator as rqt
from commons import conf, error_conf


logger = logging.getLogger('position')


class PositionDetails(APIView):
    """
    Get position detail.
    """
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        position_response = {}
        get_position_url = conf.BASE_URL + "api/get/position/"

        data_list = json.dumps(request.data.get("login"))
        data_list = data_list.replace("[", "(")
        data_list = data_list.replace("]", ")")

        get_position_data = {
            "user_login": data_list
        }
        try:
            position_response = requests.post(url=get_position_url,
                                              data=get_position_data)
        except:
            return Response(position_response,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        if position_response.status_code == 200:
            position_resp = rqt.list_position_response_translator(
                position_response.json().get("position_details"))
            return Response(position_resp)

        return Response(error_conf.PROBLEM_WITH_CORE,
                        status=status.HTTP_412_PRECONDITION_FAILED)
