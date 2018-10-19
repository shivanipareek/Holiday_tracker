#!/usr/bin/python

"""
    This script Required 12 parameter, sequence of parameter must be : first_name, last_name
    pr_position_id, position_id, Login,  phone_num, position_type SM_position_id
    SM_login, SM_f_name, SM_l_name, Account_id(must be an Array)
"""

import json,os,sys,requests

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
sys.path.append(rootDir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "volvo_core.settings")

import django
django.setup()

import delete_static_url

SM_USER = "SM"

SR_USER = "SR"

SOLR_COLLECTIONS = {

    "position": "POSITION",
    "user_hier": "USER_HIER"
}

SOLR_BASE_URL = "http://54.191.238.158:8983/solr/"


def __get_created_dt():
    from datetime import datetime
    curr_datetime = datetime.now()

    return curr_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def _unescape_values(translated_data):
    from HTMLParser import HTMLParser
    htmlparser = HTMLParser()
    updated_dict = {}

    for k, v in translated_data.iteritems():
        updated_dict[k] = htmlparser.unescape(v)

    return updated_dict


def _request_solr(collection, data, operation):
    solr_add_url = SOLR_BASE_URL + collection + "/update"

    request_data = {
        "add": {
            "commitWithin": 1000,
            "overwrite": True,
            "boost": 1.0,
            "doc": data,
        }}

    header = {
        "Content-Type": "application/json"
    }

    res = requests.post(
        solr_add_url,
        data=json.dumps(request_data),
        headers=header
    )

    return True if res.status_code == 200 else False


def add_data_to_solr(translated_data, collection):
    ret = False

    collection_name = SOLR_COLLECTIONS.get(collection)

    ret = _request_solr(collection_name, translated_data, "add")

    return ret


def create_user_hier_solr_request_translator(user_data):
    input_data = {}

    input_data["PostnPREmpFstName_s"]    = user_data.get("sr_first_name","")
    input_data["PostnPREmpLastName_s"]   = user_data.get("sr_last_name","")
    input_data["PrPostnID_s"]            = user_data.get("sr_pr_pos_id","")
    input_data["PostnID_s"]              = user_data.get("sr_position_id","")
    input_data["Login_s"]                = user_data.get("login","")
    input_data["PostnPREmpCellphNnum_s"] = user_data.get("phone_num","")
    input_data["PostnType_s"]            = user_data.get("position_type","")
    input_data["Created_dt"]             = __get_created_dt()
    input_data["DsmPostnID_s"]           = user_data.get("sm_pos_id","")
    input_data["DsmLogin_s"]             = user_data.get("sm_login","")
    input_data["DsmName_s"]              = user_data.get("sm_name","")
    input_data["DealerCode_s"]           = user_data.get("dealer_code","")
    input_data["ROW_ID"]                 = user_data.get("sr_position_id", "")

    return (input_data)


def create_position_solr_request_translator(user_data):
    input_data = {}

    input_data["PostnPREmpFstName_s"]    = user_data.get("sr_first_name","")
    input_data["PostnPREmpLastName_s"]   = user_data.get("sr_last_name","")
    input_data["PrPostnID_s"]            = user_data.get("sr_pr_pos_id","")
    input_data["PostnID_s"]              = user_data.get("sr_position_id","")
    input_data["Login_s"]                = user_data.get("login","")
    input_data["PostnPREmpCellphNnum_s"] = user_data.get("phone_num","")
    input_data["PostnType_s"]            = user_data.get("position_type","")
    input_data["Created_dt"]             = __get_created_dt()
    input_data["AccountId_ss"]           = user_data.get("account_id",[])
    input_data["DealerCode_s"]           = user_data.get("dealer_code","")
    input_data["ROW_ID"]                 = user_data.get("sr_position_id", "")

    return (input_data)


def valid_sm_user_check(sm_pos_id):
    sm_pos_id = sm_pos_id

    position_solr_query = SOLR_BASE_URL + delete_static_url.CHECK_VALID_SM_USER_URL
    position_data_url = position_solr_query % sm_pos_id
    position_data = requests.get(position_data_url)

    if position_data.status_code == 200:
        position_data_json = position_data.json()
        position_data_json = position_data_json.get("response", {}).get("docs",[])
        if position_data_json:
            return True
    return False


def add_user_pos_to_solr(user_data):

    valid_user = True

    if user_data.get("position_type") == SR_USER:
        if user_data.get("sm_pos_id"):
            valid_user = valid_sm_user_check(user_data.get("sm_pos_id"))
        else:
            return False

    if valid_user:

        position_solr_data = create_position_solr_request_translator(user_data)
        if add_data_to_solr(position_solr_data, collection="position"):

            if user_data.get("position_type") == SR_USER:
                user_hier_data = create_user_hier_solr_request_translator(
                    user_data)

                if add_data_to_solr(user_hier_data, collection="user_hier"):
                    return True
            else:
                return True
        return False


def user_data_translator(user_data):

    if user_data:
        accounts =  user_data[11]
        account_list = accounts.strip('[]').split(',')

        user_data = {
            "sr_first_name": user_data[0],
            "sr_last_name": user_data[1],
            "sr_pr_pos_id": user_data[2],
            "sr_position_id": user_data[3],
            "login": user_data[4],
            "phone_num": user_data[5],
            "position_type": user_data[6],
            "sm_pos_id": user_data[7],
            "sm_login": user_data[8],
            "sm_name": user_data[9] + user_data[10],
            "dealer_code":user_data[12],
            "account_id":account_list
        }

        return user_data
    return False


if __name__ == '__main__':

    try:

        print "This script Required 12 parameter, sequence of parameter must be: \n first_name \n last_name" \
              "\n pr_position_id \n position_id \n Login \n phone_num \n position_type \n SM_position_id " \
              "SM_login \n SM_f_name \n SM_l_name \n Account_id(must be an Array eg. '[1-5NUDNS,1-5NUDNT]' )"

        data = sys.argv[1:]
        data = user_data_translator(data)
        if data:
            if add_user_pos_to_solr(data):
                print "User Added Successfully"

            else:
                print "Failed to add user on SOLR"

    except Exception as ae:
        # logger.info("Script execution failed: " + str(ae))
        msg = "Exception: " + str(ae)
