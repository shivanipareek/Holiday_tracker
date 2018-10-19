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
import json
import requests

from commons import conf
from datetime import datetime


def _request_solr(collection, data, operation):
    solr_add_url = conf.SOLR_BASE_URL + collection + "/update"

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


def _get_from_solr(collection, field, value, rows=1, start=0):
    field_filter = field + ":" + value
    contact_data = []

    solr_contact_get_url = conf.SOLR_BASE_URL + collection + "/select?indent=on&q=%s&rows=%s&start=%s&wt=json&fl=*_s,*_i,*_dt,*_ss,ROW_ID,contentType"
    solr_contact_get_url = solr_contact_get_url % (field_filter, rows, start)
    contact_response = requests.get(solr_contact_get_url)

    if contact_response.status_code == 200:
        contact_response = contact_response.json()
        contact_data = contact_response.get('response').get('docs')
        if contact_data:
            contact_data = contact_data[0]
    return contact_data


def _get_list_from_solr(collection, field, value, sort_by_field=None,
                        sort=None):
    field_filter = field + ":" + value
    sort_field = "Due_dt%20desc"
    contact_data = []
    solr_contact_get_url = conf.SOLR_BASE_URL + collection + "/select?indent=on&q=%s&wt=json&sort=%s&fl=*_s,*_i,*_dt,*_ss,ROW_ID,contentType"

    if sort_by_field and sort:
        sort_field = sort_by_field + "%20" + sort
        solr_contact_get_url = conf.SOLR_BASE_URL + collection + "/select?indent=on&q=%s&wt=json&sort=%s&fl=*_s,*_i,*_dt,*_ss,ROW_ID,contentType"
    solr_contact_get_url = solr_contact_get_url % (field_filter, sort_field)

    contact_response = requests.get(solr_contact_get_url)

    if contact_response.status_code == 200:
        contact_response = contact_response.json()
        contact_data = contact_response.get('response').get('docs')

    return contact_data


def __get_created_dt():

    curr_datetime = datetime.now()
    # ist = pytz.timezone('Asia/Kolkata')
    # utc_datetime = ist.localize(curr_datetime)
    #
    # utc = pytz.timezone('UTC')
    # utc_datetime = utc_datetime.astimezone(utc)
    #
    # return utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    return curr_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def _unescape_values(translated_data):
    from HTMLParser import HTMLParser
    htmlparser = HTMLParser()
    updated_dict = {}

    for k, v in translated_data.iteritems():
        updated_dict[k] = htmlparser.unescape(v)

    return updated_dict


def solr_query_space_updator(data):
    if " " in data:
        data = data.replace(" ", "\%20")

    return data


def update_to_solr_date_format(data):
    updated_date = ""
    if data:
        updated_date = datetime.strptime(data, '%m/%d/%Y %S:%M:%H').strftime('%Y-%m-%dT%H:%M:%SZ')
    return updated_date
