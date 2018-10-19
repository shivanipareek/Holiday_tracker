import logging

from opty.utils import (
    get_opty_from_solr,
)
from VolvoCore import static_solr_urls
from opty import solr_request_translator as srt
from opty import solr_utility

logger = logging.getLogger("opty")


def update_opty_data_on_solr(data,solr_opty_id):

    opty_detail_url = static_solr_urls.OPTY_DETAIL_FOR_UPDATE_URL

    sol_opty_object = get_opty_from_solr(
        opty_detail_url,
        solr_opty_id)

    if sol_opty_object:

        updated_opty_dict = srt.update_opty_solr_request_translator(data,
                                                                     sol_opty_object[0])

        if solr_utility.addopty_solr(updated_opty_dict):
            logger.info("Data pushed to solr.")


