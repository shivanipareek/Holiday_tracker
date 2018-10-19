import logging

from commons import conf
from commons.solr_helper import (
    _request_solr
)

def addopty_solr(translated_data):

    ret = False



    collection_name = conf.SOLR_COLLECTIONS.get("opty_test")

    # Opty solr
    ret = _request_solr(collection_name, translated_data, "add")

    return ret