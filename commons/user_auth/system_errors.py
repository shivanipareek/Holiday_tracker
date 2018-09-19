# /********************************************************************************
# * AUDETEMI INC. ("COMPANY") CONFIDENTIAL
# *_______________________________________
# *
# * Unpublished Copyright (c) 2015-2017 [AUDETEMI INC].
# * http://www.audetemi.com.
# * All Rights Reserved.
# *
# * NOTICE:  All information contained herein is, and remains the property of COMPANY. * The intellectual and #technical concepts contained herein are proprietary to COMPANY * and may be covered by U.S. and Foreign Patents, #patents in process, and are
# * protected by trade secret or copyright law.
# * Dissemination of this information or reproduction of this material is strictly
# * forbidden unless prior written permission is obtained from COMPANY.
# * Access to the source code contained herein is hereby forbidden to anyone except
# * current COMPANY employees, managers or contractors who have executed
# * Confidentiality and Non-disclosure agreements explicitly covering such access.
# *
# * The copyright notice above does not evidence any actual or intended publication or * disclosure of this source #code, which includes information that is confidential
# * and/or proprietary, and is a trade secret, of the COMPANY.
# *
# * ANY SUB-LICENSING, REPRODUCTION, REVERSE ENGINEERING, DECOMPILATION, MODIFICATION, * DISTRIBUTION, PUBLIC #PERFORMANCE, OR PUBLIC DISPLAY OF OR THROUGH USE OF THIS
# * SOURCE CODE WITHOUT THE EXPRESS WRITTEN CONSENT OF COMPANY IS STRICTLY PROHIBITED,
# * AND IN VIOLATION OF APPLICABLE LAWS AND INTERNATIONAL TREATIES.  THE RECEIPT OR
# * POSSESSION OF THIS SOURCE CODE AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY * ANY RIGHTS TO REPRODUCE, #DISCLOSE OR DISTRIBUTE ITS CONTENTS, OR TO MANUFACTURE,
# * USE, OR SELL ANYTHING THAT IT MAY DESCRIBE, IN WHOLE OR IN PART.
# */
from commons import error_conf
from commons.user_auth.models import UserDeviceInformation
from commons import conf


def check_for_login_input_error(data):
    ###
    ## Error Handling For Login API
    ###

    if not data.get('username'):
        return error_conf.USERNAME_NOT_PROVIDED

    elif not data.get('password'):
        return error_conf.PASSWORD_NOT_PROVIDED

    return False


def check_for_device_id(data):
    """
    Check of marching refresh token and device id for refreshibg token.
    """

    refresh_token = data.get("refresh_token", None)
    device_id = data.get("device_id", None)
    if refresh_token:
        user_device = UserDeviceInformation.objects.filter(device=device_id)
        if user_device:
            user_device = user_device[0]
            if user_device.device == device_id:
                return False

    return error_conf.INVALID_DEVICE_ID_PROVIDED


def check_for_logout_errors(data):
    if not data.get('refresh_token'):
        return error_conf.REFRESH_TOKEN_NOT_PROVIDED

    if not data.get('device_id'):
        return error_conf.DEVICE_ID_NOT_PROVIDED

    return False


def check_for_user_lang_input(data):
    if not data.get("language"):
        return error_conf.LANGUAGE_NOT_PROVIDED

    return False


def check_for_user_hier_errors(data):
    if not data.get("position_type"):
        return error_conf.POSITION_TYPE_NOT_PROVIDED

    if not data.get("position_id"):
        return error_conf.POSITION_ID_NOT_PROVIDED

    return False


def check_for_user_position_errors(data):
    if not data.get("pos_id"):
        return error_conf.POSITION_ID_NOT_PROVIDED

    return False


def add_user_error_checks(data):

    if data.get("position_type") == conf.SR_USER:

        if not data.get("sm_pos_id"):
            return error_conf.SM_POSITION_ID_NOT_PROVIDED
        if not data.get("sm_login"):
            return error_conf.SM_LOGIN_NOT_PROVIDED
        if not data.get("sm_f_name"):
            return error_conf.SM_FIRST_NAME

    if not data.get("sr_first_name"):
        return error_conf.SR_FIRST_NAME
    if not data.get("sr_pr_pos_id"):
        return error_conf.SR_PR_POSITION_ID_NOT_PROVIDED
    if not data.get("sr_position_id"):
        return error_conf.SR_POSITION_ID_NOT_PROVIDED
    if not data.get("login"):
        return error_conf.SR_LOGIN_ID_NOT_PROVIDED
    if not data.get("phone_num"):
        return error_conf.SR_PH_NUM_NOT_PROVIDED
    if not data.get("position_type"):
        return error_conf.POSITION_TYPE_NOT_PROVIDED
    if not data.get("account_id"):
        return error_conf.ACCOUNT_ID_NOT_PROVIDED

    return False

def delete_account_error_checks(data):

    if not data.get("account_id"):
        return error_conf.ACCOUNT_ID_NOT_PROVIDED
    return False
