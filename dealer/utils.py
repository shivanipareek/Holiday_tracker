import requests
from commons import conf
# from commons.conf import SOLR_BASE_URL
# from VolvoCore import static_solr_urls
from commons.solr_helper import (
    _request_solr
)

def get_dealer_data(dealer_id):

    dealer_data = []
    dealer_details = {
            "DealerCode": "C669",
            "Dealer_ID" : "CA445",
            "Position_ID": "1-4S5B"
        }

    if dealer_id != dealer_details.get("Dealer_ID"):
        return False

    else:
        dealer_data.append(dealer_details)
        return dealer_data

def add_dealer_to_solr(translated_data):

    ret = False

    collection_name = conf.SOLR_COLLECTIONS.get("opty_test")

    # Opty solr
    ret = _request_solr(collection_name, translated_data, "add")

    return ret