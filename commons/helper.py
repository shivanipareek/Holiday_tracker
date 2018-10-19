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
import datetime
import json
from VolvoCore import system_messages
from conf import AUDETEMI_WSDL_PASS,AUDETEMI_WSDL_USERNAME


def datetime_to_epoch():
    dt = datetime.now()
    epoch = datetime.datetime.utcfromtimestamp(0)
    epoch_time = (dt - epoch).total_seconds() * 1000.0
    return int(epoch_time)


def get_created_user_detail_translator(data):
    input_data = {}

    user_details = data.get("user_details", {})

    if user_details.get("created_by_firstname"):
        input_data["CreatedByFirstName_s"] = user_details.get("created_by_firstname")

    if user_details.get("created_by_lastname"):
        input_data["CreatedByLastName_s"] = user_details.get("created_by_lastname")

    if user_details.get("created_user_pos_type"):
        input_data["CreatedByPostnType_s"] = user_details.get("created_user_pos_type")

    return input_data


def _list_to_solr_filter(data):
    data_list = json.dumps(data)
    data_list = data_list.replace("[", "(")
    data_list = data_list.replace("]", ")")
    return data_list


def soap_keys_translator(prefix_variable,data):

    if data:
        for key, value in data.items():
            updated_key = key.replace(prefix_variable, "")
            data[updated_key] = value
            del data[key]
            if not data.get(updated_key):
                del data[updated_key]

        return data
    return {}

def update_to_siebel_date_format(data):
    updated_date = ""
    if data:
        updated_date = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y %S:%M:%H')
    return updated_date

def wsdl_authentication(data):

    if not data:
        return system_messages.PLEASE_PROVIDE_USERNAME_PASS

    user_name = data.get("username","")
    password = data.get("password","")

    if user_name != AUDETEMI_WSDL_USERNAME:
        return system_messages.PLEASE_PROVIDE_VALID_USERNAME

    if password != AUDETEMI_WSDL_PASS:
        return system_messages.INVALID_PASSWORD

    return False

def auth_soap_keys_translator(prefix_variable,data):

    if data:
        for key, value in data.items():
            updated_key = key.replace(prefix_variable, "")
            data[updated_key] = value
            if not data.get(updated_key):
                del data[updated_key]

        return data
    return {}
