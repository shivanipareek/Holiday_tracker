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

from VolvoCore import system_messages


def validate_position_data(data):
    if not data.get("user_login"):
        return system_messages.POSITION_ID_NOT_PROVIDED

    return False

def check_for_sr_under_sm_errors(data):
    if not data.get("position_id"):
        return system_messages.POSITION_ID_NOT_PROVIDED
    if not data.get("login_id"):
        return system_messages.LOGIN_NOT_PROVIDED

    return False
