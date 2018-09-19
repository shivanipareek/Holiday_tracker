# -*- coding: utf-8 -*-

# */
import json
import logging
from datetime import datetime
import requests

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import helper
from commons import error_conf, success_conf, conf
from commons.position import response_translator as rqt
from commons.user_auth import system_errors
from commons.user_auth.models import (
    UserDeviceInformation,
    UserDetailInformation, UserPositionDeviceDetails)
from commons.user_auth.serializers import UserDetailInformationSerializer

logger = logging.getLogger('user_auth')

class LoginView(APIView):
    """
    Login API
    """

    def post(self, request, format=None):

        logger.info("Login start " + str(datetime.now()))
        data = request.data
        error_checks = system_errors.check_for_login_input_error(request.data)

        logger.info("Error checks done " + str(datetime.now()))
        # try:
        if not error_checks:

                username = data.get('username')
                password = data.get('password')
                app_name = data.get('app_name')

                # Verify entered credentials with Volvo
                """
                TODO: Need to remove below hard coded. currently we 
                have only 1 volvo user so added this condition.
                """

                # volvo_auth = helper.authenticate_with_volvo("xw68319",password)
                # logger.info("........Volvo Auth Response.......")
                # logger.info(volvo_auth)
                # if not volvo_auth:
                #     return Response(error_conf.INVALID_CREDENTIALS,
                #                     status=status.HTTP_412_PRECONDITION_FAILED)
                user_device = data.get("device_id", None)
                user_app_version = data.get("app_version", None)
                # app_name = data.get("app_name", None)

                logger.info(
                    "Authenticating user details from RDS " + str(datetime.now()))

                # If username / password entered matches with the system stored creds,
                # go ahead and generate new token for existing user.
                user = authenticate(username=username, password=password)

                if user:
                    logger.info("User fetched successfully " + str(datetime.now()))
                    helper.validate_login_request(request, user)

                    logger.info("Generating oauth token " + str(datetime.now()))
                    token = helper.generate_oauth_token(self, username, password)
                    if token.status_code != 200:
                        return Response(error_conf.INVALID_CREDENTIALS,
                                        status=status.HTTP_412_PRECONDITION_FAILED)
                else:
                    logger.info("Authentication with system has failed.")

                    return Response(error_conf.INVALID_CREDENTIALS,
                                        status=status.HTTP_412_PRECONDITION_FAILED)


                token_information = json.loads(token._content)
                access_token = token_information.get("access_token")
                refresh_token = token_information.get("refresh_token")


                try:
                    user_info = UserDeviceInformation.objects.get(
                        user=user,
                        app_name=app_name,
                        device=user_device)
                    user_info.access_token = access_token
                    user_info.refresh_token = refresh_token

                except:
                    user_info = UserDeviceInformation(user=user,
                                                      app_name=app_name,
                                                      access_token=access_token,
                                                      refresh_token=refresh_token)
                try:
                    user_detail = UserDetailInformation.objects.get(user=user)
                except:
                    user_detail = UserDetailInformation(user=user,
                                                        favourite_opty=[],
                                                        favourite_lead=[],
                                                        user_account=[],
                                                        favourite_accounts="",
                                                        favourite_contacts="")


                user_detail.save()
                user_detail = UserDetailInformation.objects.get(user=user)
                user_detail = UserDetailInformationSerializer(user_detail)

                if user_device:
                    user_info.device = user_device
                if user_app_version:
                    user_info.app_version = user_app_version
                if app_name:
                    user_info.app_name = app_name

                logger.info(
                    "Save user data and it's position detals back to RDS " + str(
                        datetime.now()))
                user_info.save()
                logger.info(
                    "User data saved successfully " + str(datetime.now()))

                user_data = user_detail.data.get("user", {})
                user_data["language"] = user_detail.data.get("language")

                # return Response(user_detail.data,status=status.HTTP_200_OK)
                #
                return Response({"token": token_information,
                                 "user_details": user_data
                                 },status=status.HTTP_200_OK)
        # except:
        #     import traceback
        #     traceback.print_exc()

        return Response(error_checks,status=status.HTTP_412_PRECONDITION_FAILED)


class LogoutView(APIView):
    """
    Logout API.
    """

    def post(self, request, *args, **kwargs):
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'token': request.META['HTTP_AUTHORIZATION'][7:],
                   'token_type_hint': 'access_token',
                   'client_id': client_id,
                   'client_secret': client_secret}

        host = self.request.get_host()

        return Response(requests.post('http://' + host +
                                      "/o/revoke_token/", data=payload,
                                      headers=headers))


class RefreshToken(APIView):
    """
    Refresh Token API.
    """

    def post(self, request, *args, **kwargs):

        data = request.data
        # check if refresh token is coming from same device.

        data_errors = system_errors.check_for_logout_errors(data)

        if not data_errors:
            error_checks = system_errors.check_for_device_id(data)

            if not error_checks:

                device_id = data.get("device_id")
                app_name = data.get("app_name")
                user_device = UserDeviceInformation.objects.filter(
                    device=device_id, app_name=app_name)
                if user_device:
                    response = helper.generate_refresh_token(self)

                    if response.status_code == 200:
                        response_json = response.json()
                        user_device = user_device[0]
                        user_device.refresh_token = response_json.get(
                            "refresh_token")
                        user_device.access_token = response_json.get(
                            "access_token")
                        user_device.save()
                        return Response(response_json)

                return Response(error_conf.INVALID_REFRESH_TOKEN_PROVIDED,
                                status=status.HTTP_412_PRECONDITION_FAILED)
            return Response(error_checks,
                            status=status.HTTP_412_PRECONDITION_FAILED)
        return Response(data_errors,
                        status=status.HTTP_412_PRECONDITION_FAILED)


class UserLanguageView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        data = request.data
        error_check = system_errors.check_for_user_lang_input(data)

        if error_check:
            return Response(error_check,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        user_details = UserDetailInformation.objects.get(user=request.user)

        if user_details:
            user_details.language = request.data.get('language')
            user_details.save()

            return Response(success_conf.LANGUAGE_UPDATED_SUCCESSFULLY)


