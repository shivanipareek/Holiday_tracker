def create_dealer_request_translator(data):
    input_data = {}

    input_data["DealerCode_s"] = data.get("DealerCode", "")
    input_data["DealerId_s"] = data.get("DealerId", "")
    input_data["PositionId_s"] = data.get("PositionId", "")

    return input_data


def update_dealer_translator(data, updated_dict):

         if data.get("DealerCode"):
             updated_dict["DealerCode_s"] = data.get("DealerCode")
         # if data.get("OrgType"):
         #     updated_dict["OrgType_s"] = data.get("OrgType")
         # if data.get("PosSubType"):
         #     updated_dict["PosSubType_s"] = data.get("PosSubType")
         if data.get("PositionId"):
             updated_dict["PositionId_s"] = data.get("PositionId")
         # if data.get("TM2EnableFlag"):
         #     updated_dict["TM2EnableFlag_s"] = data.get("TM2EnableFlag")
         # if data.get("VssEnableFlag"):
         #     updated_dict["VssEnableFlag_s"] = data.get("VssEnableFlag")
         # if data.get("DealerBrandName"):
         #     updated_dict["DealerBrandName_s"] = data.get("DealerBrandName")
         # if data.get("BrandIsPrimary"):
         #     updated_dict["BrandIsPrimary_s"] = data.get("BrandIsPrimary")
         # if data.get("CustSatisfactionScore"):
         #     updated_dict["CustSatisfactionScore_s"] = data.get("CustSatisfactionScore")

         return updated_dict
