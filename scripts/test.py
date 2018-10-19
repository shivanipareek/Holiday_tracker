from datetime import datetime
import json,os,sys,requests




def get_data():

    input_data = {
        "Activity_name_s":"XYZ",
        "Activity_ID_s":"101",
        "Position_ID_s":"A1",
        "date_dt":"2018-09-11T00:00:00Z",
        "ROW_ID":"0088d10a-ee1a-4d2f-b81c-39d764010b87"
    }
    return (input_data)

def push_data_to_solr(data):

    final_list = []
    final_list.append(data)

    push_solr_url = "http://54.200.153.229:8983/solr/TEST_ACTIVITY/update?commit=true"

    try:
        try:
            response_data = requests.post(url=push_solr_url,
                                          data=json.dumps(final_list),
                                          headers={'content-type': 'application/json'})

            if response_data.status_code == 200:
                print '\nDATA pushed to Solr'
            else:
                print "\nelse: SOLR response"
        except Exception as e:
            print "kjshdfkjaf",e
    except Exception as ie:
        print "Exception:!!! ", str(ie)


if __name__ == '__main__':

    try:
        data = get_data()
        if data:
            push_data_to_solr(data)
        else:
            print "failed to fetch data"

    except Exception as e:
        msg = "operation failed"