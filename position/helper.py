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
import requests

from commons import conf
from VolvoCore import static_solr_urls



def get_dse_under_dsm(user_login,position_id):
    dse_detail_url = conf.SOLR_BASE_URL + static_solr_urls.GET_DSE_UNDER_DSM_URL
    dse_data = "%22" + user_login + "%22"
    dse_detail_url = dse_detail_url % (dse_data,position_id)
    dse_response_data = []

    dse_response = requests.get(dse_detail_url)

    if dse_response.status_code == 200:
        dse_response_data = dse_response.json()
        dse_response_data = dse_response_data.get('response', {}).get('docs', [])
    return dse_response_data


def get_dsm(user_login,position_id):
    dsm_detail_url = conf.SOLR_BASE_URL + static_solr_urls.GET_DSM_URL
    dse_data = "%22" + user_login + "%22"
    dsm_detail_url = dsm_detail_url % (dse_data,position_id)
    dsm_response_data = []

    dsm_response = requests.get(dsm_detail_url)

    if dsm_response.status_code == 200:
        dsm_response_data = dsm_response.json()
        dsm_response_data = dsm_response_data.get('response', {}).get('docs', [])
    return dsm_response_data
