# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import logging
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import system_errors
from commons import conf
from helper import (
    get_dse_under_dsm,
    get_dsm
)
# from opty.utils import (
#     _list_to_solr_filter
# )
# from position.utils import (
#     get_position_details,
#     append_list_of_key
# )
from VolvoCore import static_solr_urls
from VolvoCore import system_messages

logger = logging.getLogger("position")

# Create your views here.


class GetPosition(APIView):
    """
    Get Position Details
    """

    def post(self, request, *args, **kwargs):

        data = request.data
        position_details = []
        error_checks = system_errors.validate_position_data(data)
        response_object = {}

        if error_checks:
            return Response(error_checks,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        user_login = data.get('user_login')

        position_detail_url = conf.SOLR_BASE_URL + static_solr_urls.GET_POSITION_URL
        position_data = user_login
        position_detail_url = position_detail_url % (position_data)

        campaign_response = requests.get(position_detail_url)
        if campaign_response.status_code == 200:

            campaign_data = campaign_response.json()
            campaign_data = campaign_data.get("response", {}).get("docs", [])

            if campaign_data:
                position_details = campaign_data

                # Retriving DSE and DSM details based on positions
                if position_details:
                    position_type = position_details[0].get("PostnType_s")
                    position_id = position_details[0].get("PostnID_s","")

                    if position_type.upper() == conf.SM_USER:
                        response_object["dse_list"] = get_dse_under_dsm(
                            user_login,position_id)
                    if position_type.upper() == conf.SR_USER:
                        dsm_data = get_dsm(user_login,position_id)
                        if dsm_data:
                            response_object["dsm"] = dsm_data[0]
                        else:
                            response_object["dsm"] = {}

            response_object["position_details"] = position_details

            return Response(response_object)

        return Response(system_messages.GENERIC_API_FAILURE)