def competitor_siebel_req_translator(data):


    final_tuple = (
        data.get("Login_s", ""),
        data.get("DealerCode_s", "Macasa"),
        data.get("SiebelOptyId_s", ""),
        data.get("SaleStage", ""),
        data.get("PositionId_s", ""),
        data.get("Make_s", "Renault"),
        data.get("Name_s", ""),
        data.get("EstQty_s", ""),
        data.get("ComModel_s", ""),
        data.get("CompetitorsPrice_s", ""),
        data.get("SalesType_s", ""),
        data.get("ComComments_s", ""),
    )

    return final_tuple

def activity_siebel_req_translator(data):
    input_data = (
        data.get("Login_s", ""),
        data.get("DealerCode_s", "Macasa"),
        data.get("TurnInLeadId_s", ""),
        data.get("MarketingLeadId_s", ""),
        data.get("SeibelActivityId_s", ""),
        data.get("AccountId_s", ""),
        data.get("Type_s", "").title(),
        data.get("Status_s", "").title(),
        data.get("Comment_s", ""),
        data.get("Description_s", ""),
        # update_to_siebel_date_format(data.get("Due_dt", "")),
        # update_to_siebel_date_format(data.get("CompletedDate_dt", "")),
        data.get("PrimaryOwnedBy_s", ""),
        data.get("DoneFlag_s", ""),
        data.get("siebel_opty_id", ""),
        # update_to_siebel_date_format(data.get("PlannedDate_dt", "")),
        # update_to_siebel_date_format(data.get("PlannedCompleted_s", "")),
        data.get("CrmActIdebtifier_s", ""),
        data.get("SubType_s", ""),
        data.get("Proceed_s", "")
    )

    return (input_data)

def contact_siebel_req_translator(data):

    final_tuple = (
        data.get("Login_s", ""),
        data.get("DealerCode_s","Macasa"),
        data.get("SiebelContactId_s",""),
        data.get("AccountId_s", ""),
        data.get("CellularPhone_s",""),
        data.get("EmailAddress_s",""),
        data.get("FirstName_s",""),
        data.get("JobTitle_s",""),
        data.get("LastName_s",""),
        data.get("CRMContactDMU_s",""),
        data.get("CRMContactsHobby_s", ""),
    )

    return final_tuple

def opty_siebel_req_translator(data):
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
        # update_to_siebel_date_format(data.get("DeliveryDate_s", "")),
        data.get("DealerCode_s", ""),
        data.get("SourceType_s", "New Units"),
        data.get("PositionId_s", ""),
        # update_to_siebel_date_format(data.get("ExpectedOrderDate_s", "")),
        data.get("OpportunityType", ""),
        data.get("CRMAvgUnits_s", ""),
        data.get("Quoted_s", ""),
        data.get("Reason2_s", ""),
        data.get("Reason1_s", ""),
        data.get("Reason3_s", ""),
        data.get("TurnInLeadId_s", "")
    )
    return create_opty_data
