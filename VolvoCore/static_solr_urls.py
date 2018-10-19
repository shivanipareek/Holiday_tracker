GET_OPTY_BY_POS = "OPTY/select?indent=on&q=PositionId_s:%s&wt=json&rows=10000"

GET_ACC_BY_POS = "POSITION/select?fl=AccountId_ss&indent=on&q=PostnID_s:%s&wt=json&rows=10000"

GET_ACC_LIST = "ACCOUNT/select?fl=Name_s,Latitude_s,Longitude_s,AccountId_s&indent=on&q=AccountId_s:%s&wt=json&rows=10000"

GET_POSITION_URL = "POSITION/select?indent=on&q=Login_s:%s&wt=json&rows=100000"

OPTY_DETAIL_FOR_UPDATE_URL = "OPTY/select?indent=on&q=OptyId_s:%s&wt=json&rows=100000&fl=*_s,*_i,*_dt,*_ss,ROW_ID,contentType"

GET_ACCTIVITY_SYNC = "ACCTIVITY/select?indent=on&q=SyncStatus_s:false&wt=json"

GET_OPTY_SYNC = "OPTY/select?indent=on&q=SyncStatus_s:false&wt=json"

GET_CONTACT_SYNC = "CONTACT/select?indent=on&q=SyncStatus_s:false&wt=json"

GET_COMPETITOR_SYNC = "COMPETITOR/select?indent=on&q=SyncStatus_s:false&wt=json"

GET_OPTY_BY_POSITION = "OPTY/select?fl=OptyId_s,OpportunityName_s,Status_s,SalesStage_s,Created_dt&indent=on&q=PositionId_s:%s&wt=json&rows=10000"

GET_COMPETITOR_DETAILS = "COMPETITOR/select?indent=on&q=OptyID_s:%s&wt=json&rows=10000"

GET_OPTY_ID = "OPTY/select?indent=on&q=OptyId_s:%s&wt=json"

DEALER_LIST_URL = "DEALER/select?indent=on&q=DealerId_s:%s&wt=json&fl=*_s,*_i,*_dt,*_ss,ROW_ID,contentType&rows=10000"