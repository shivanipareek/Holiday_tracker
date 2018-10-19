DELETE_SOLR_URL = "/update?commit=true&stream.body=<delete><query>%s</query></delete>"

FILTER_SOLR_DATA_URL = "/select?indent=on&q=%s&wt=json&rows=10000"

CHECK_SOLR_DATA = "/select?indent=on&q=%s&wt=json"

CHECK_VALID_SM_USER_URL = "POSITION/select?indent=on&q=PostnID_s:%s%%20AND%%20PostnType_s:SM&wt=json&rows=1000"
