from commons.helper import update_to_siebel_date_format

def __to_tuple_for_create_opty(data):

    create_opty_data = (

        data.get("Login_s", ""),
        data.get("Dealer", "Macasa"),
        data.get("MarketingLeadId_s", ""),
        data.get("SiebelOptyId_s", ""),  # BoomBoxId
        data.get("AccountName_s", ""),
        data.get("AccountId_s", ""),
        data.get("OpportunityName_s", ""),
        data.get("SalesStage_s", ""),
        data.get("Status_s", ""),
        data.get("Comments_s", ""),
        data.get("EstimatedQuantity_s", ""),
        data.get("Make_s", "Renault"),
        data.get("ProductCategory_s", ""),
        # for demo/poc we use this key, Need to update the key with "Product Category" key
        data.get("WinProbability_s", "10"),
        update_to_siebel_date_format(data.get("DeliveryDate_s", "")),
        data.get("DealerCode_s", ""),
        data.get("SourceType_s", "New Units"),
        data.get("PositionId_s", ""),
        update_to_siebel_date_format(data.get("ExpectedOrderDate_s", "")),
        data.get("OpportunityType", ""),
        data.get("CRMAvgUnits_s", ""),
        data.get("Quoted_s", ""),
        data.get("Reason2_s", ""),
        data.get("Reason1_s", ""),
        data.get("Reason3_s", ""),
        data.get("TurnInLeadId_s", "")

    )
    return create_opty_data
