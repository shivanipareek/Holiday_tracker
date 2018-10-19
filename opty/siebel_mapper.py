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

class BaseClass(object):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True,
                          indent=4)

class OptyRequestMapper(BaseClass):

    def __init__(self, data):
        self.Login_s             = data.get("Login_s", "")
        self.AccountId_s         = data.get("AccountId_s", "")
        self.AccountName_s       = data.get("AccountName_s", "")
        self.OpportunityName_s   = data.get("OpportunityName_s", "")
        self.EstimatedQuantity_s = data.get("EstimatedQuantity_s", "")
        self.SalesStage_s        = data.get("SalesStage_s", "")
        self.Status_s            = data.get("Status_s", "")
        self.Model_s             = data.get("Model_s", "")
        self.ExpectedOrderDate_s = data.get("ExpectedOrderDate_s", "")
        self.DeliveryDate_s      = data.get("DeliveryDate_s", "")
        self.Comments_s          = data.get("Comments_s", "")
        self.Reason1_s           = data.get("Reason1_s", "")
        self.CRMAvgUnits_s       = data.get("CRMAvgUnits_s", "")
        self.Quoted_s            = data.get("Quoted_s", "")
        self.Reason2_s           = data.get("Reason2_s", "")
        self.Reason3_s           = data.get("Reason3_s", "")
        self.LastUpdated_dt      = data.get("LastUpdated_dt", "")
        self.DealerCode_s        = data.get("DealerCode_s", "")
        self.OptyId_s            = data.get("OptyId_s", "")
        self.MarketingLeadId_s   = data.get("MarketingLeadId_s", "")
        self.TurnInLeadId_s      = data.get("TurnInLeadId_s", "")
        self.PositionId_s        = data.get("PositionId_s", "")
        self.Created_dt          = data.get("Created_dt", "")


class OptyResponseMapper(BaseClass):

    def __init__(self, data):
        self.SiebelOptyId_s = data.get("ns:BoomBoxId", "")
