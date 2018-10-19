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