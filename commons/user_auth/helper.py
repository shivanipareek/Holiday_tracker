import json
import logging
from datetime import datetime

import requests
from django.conf import settings

from commons import (
    conf
)
from models import (
    UserDetailInformation,
    UserDeviceInformation,
    UserPositionDeviceDetails
)

from VolvoSkin.settings import (
    VOLVO_CLIENT_ID,
    VOLVO_CLIENT_SECRET
)

logger = logging.getLogger("user_auth")


def generate_oauth_token(self, username, password):
    """
    This function generates access token for User.
    """

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': client_id,
               'client_secret': client_secret}
    host = self.request.get_host()

    return (requests.post(settings.SERVER_PROTOCOLS + host + "/o/token/",
                          data=payload, headers=headers))


def generate_refresh_token(self):
    """
    This function refreshes access token for User.
    """

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    refresh_token = str(self.request.data.get('refresh_token'))

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'refresh_token',
               'client_id': client_id,
               'client_secret': client_secret,
               'token type': 'Bearer',
               'refresh_token': refresh_token}
    host = self.request.get_host()

    return (requests.post(settings.SERVER_PROTOCOLS + host + "/o/token/",
                          data=payload, headers=headers))


def invalidate_existing_access_token(request, access_token):
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'token': access_token,
               'token_type_hint': 'access_token',
               'client_id': client_id,
               'client_secret': client_secret}

    host = request.get_host()

    response = requests.post('http://' + host +
                             "/o/revoke_token/", data=payload, headers=headers)

    if response.status_code == 200:
        return True
    return False


def validate_login_request(request, user):
    data = request.data
    user_device = data.get("device_id", None)
    app_name = data.get("app_name", None)
    logger.info("Validating user " + str(datetime.now()))
    user_info = UserDeviceInformation.objects.filter(user=user,
                                                     device=user_device,
                                                     app_name=app_name)
    if user_info:
        user_info = user_info[0]
        access_token = user_info.access_token
        logger.info(
            "Invalidating user token if already exists " + str(datetime.now()))
        check = invalidate_existing_access_token(request, access_token)

        if check:
            return True
        else:
            return False
    return True


####### Get Position ########
def get_position_data(data):
    position_response = {}
    get_position_url = conf.BASE_URL + "api/get/position/"

    get_position_data = {
        "user_login": data.get("user_login", "")
    }
    try:
        position_response = requests.post(url=get_position_url,
                                          data=get_position_data)
    except:
        return position_response

    if position_response.status_code == 200:
        return position_response.json()

    return position_response


def get_user_login(user):
    return user.username


def get_user_position(user):
    user = UserDetailInformation.objects.filter(user=user)

    if user:
        user = user[0].user_position_details

        return user


def get_logged_in_user_position(user):
    user = UserDetailInformation.objects.filter(user=user)

    if user:
        position_id = user[0].logged_in_pos_id

        return position_id


def get_user_account(data):
    user_account_response = {}
    get_user_acc_url = conf.BASE_URL + "api/user/account/"

    try:
        user_account_response = requests.post(url=get_user_acc_url,
                                              data=json.dumps(data),
                                              headers={
                                                  "Content-Type": "application/json"})
    except:
        return user_account_response

    if user_account_response.status_code == 200:
        return user_account_response.json()

    return user_account_response


def get_user_position_type(user):
    position_details = get_user_position(user)

    return position_details


def get_user_hier_position_data(data):
    position_response = {}
    get_position_url = conf.BASE_URL + "api/get/hier/position/"

    get_position_data = {
        "position_id": data.get("position_id", ""),
        "position_type": data.get("position_type", ""),
        "login_id":data.get("login","")
    }
    try:
        position_response = requests.post(url=get_position_url,
                                          data=get_position_data)
    except:
        return position_response
    return position_response.json()


def user_details_request_translator(position_id,user):
    if position_id and type(position_id) is list:
        position_id = position_id[0]

    user_details = {}
    user_detail  = UserPositionDeviceDetails.objects.filter(
        position_id=position_id,username=user.username)

    if user_detail:

        user_detail = user_detail[0]
        if user_detail.username:
            user_details["user_name"] = user_detail.username
        if user_detail.first_name:
            user_details["created_by_firstname"] = user_detail.first_name
        if user_detail.last_name:
            user_details["created_by_lastname"] = user_detail.last_name
        if user_detail.position_type:
            user_details["created_user_pos_type"] = user_detail.position_type

    return user_details


def get_user_position_device_detail(position_id):
    user_detail = UserPositionDeviceDetails.objects.filter(
        position_id=position_id)

    if user_detail:
        user_detail = user_detail[0]

    return user_detail


def get_user_account_by_position(position_id):

    user_account = []

    if position_id:
        user_detail = UserPositionDeviceDetails.objects.filter(
            position_id=position_id)

        if user_detail:
            user_detail = user_detail[0]
            user_account = user_detail.position_accounts

    return user_account

def authenticate_with_volvo(username,password):

    volvo_authentication_url = conf.VOLVO_AUTH_URL % (VOLVO_CLIENT_ID,
                                                      VOLVO_CLIENT_SECRET,
                                                      username,password)
    try:
        volvo_authenticate_response = requests.post(url=volvo_authentication_url)
    except ConnectionError as ce:
        return False

    logger.info(volvo_authenticate_response.status_code)
    logger.info(volvo_authenticate_response.text)

    if volvo_authenticate_response.status_code == 200 or volvo_authenticate_response.status_code == 201:
        if volvo_authenticate_response.json().get("access_token"):
            return True
        return False
    else:
        logger.error(volvo_authenticate_response.text)
        return False
