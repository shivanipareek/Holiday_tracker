import json
import logging
import requests
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from requests import ConnectionError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import (APIView)
import response_translator as rst
from commons import (
    BASE_URL,
    WriteJSONParser,
    error_conf,
)
from commons.user_auth import system_errors
from . import system_errors

logger = logging.getLogger('account')

class GetAccountByPositionID(APIView):
    parser_classes = [WriteJSONParser]
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        pos_id = request.data.get("pos_id", [])
        pos_id = {"pos_id": pos_id}
        error_checks = system_errors.check_for_acc_by_pos_input_errors(
            pos_id)

        if error_checks:
            return Response(error_checks,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        get_acc_by_pos = BASE_URL + "api/acc/by_pos/"

        try:
            response_data = requests.post(url=get_acc_by_pos,
                                          data=json.dumps(pos_id),
                                          headers={
                                              "Content-Type": "application/json"})
        except ConnectionError as ce:
            return Response(error_conf.UNABLE_TO_REACH_CORE,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        if response_data.status_code == 200:
            Acc_json_response = rst.acc_response_translator(
                response_data)
            return Response({"Result": Acc_json_response})
        return Response({"msg": "notsuccess"})
