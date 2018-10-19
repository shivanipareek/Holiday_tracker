import requests
# # import django
# from siebel import create_competitor_in_siebel
# from activity_siebel import create_activity_in_siebel
# from contact_siebel import create_contact_in_siebel
# from opty_siebel import create_opty_in_siebel
# # django.setup()

SOLR_BASE_URL = "http://54.200.153.229:8983/solr/"

SOLR_COLLECTIONS = {

    "acitivity": "ACTIVITY",
    "opty": "OPTY",
    "contact":"CONTACT",
    "competitor":"COMPETITOR"
}

def  get_solr_data(collection):

    solr_get_url = SOLR_BASE_URL + collection + "/select?indent=on&q=SyncStatus_s:%22false%22&wt=json"

    res = requests.get(url = solr_get_url,headers= {"Content-Type": "application/json"})

    if res.status_code == 200:
        response_data_json = res.json()
        res = response_data_json.get("response", {}).get("docs", [])
        return res
    return "failed"

def get_solr_collection(collection):

    ret = False
    collection_name = SOLR_COLLECTIONS.get(collection)
    ret = get_solr_data(collection_name)
    return ret

if __name__ == '__main__':

    try:
    #     temp_dict = {}

        for key, value in SOLR_COLLECTIONS.iteritems():
            print "Going for collecction--->", key
            data = get_solr_collection(collection=key)
            print data
        #     temp_dict[key] = data
        #
        # create_activity_in_siebel(temp_dict.get("ACTIVITY"))
        # create_opty_in_siebel(temp_dict.get("OPTY"))
        # create_contact_in_siebel(temp_dict.get("CONTACT"))
        # create_competitor_in_siebel(temp_dict.get("COMPETITOR"))


    except Exception as e:
        print  "operation failed" + str(e)