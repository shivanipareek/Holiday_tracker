import requests
import json
import os
import csv
import glob


solrdata = {
    "Bussiness_address_id": "BussinessAddressId_s",
    "city": "City_s",
    "country": "Country_s",
    "state": "State_s",
    "street address": "StreetAddress_s",
    "Latitude": "Latitude_s",
    "CRM Direction": "CrmDirection_s",
    "Longitude": "Longitude_s",
    "street address2": "Streetaddress2_s",
    "Postal_code": "PostalCode_s",
    "Account_id":"AccountId_s"
}

def push_data_to_solr(data):

    solr_url = "http://54.200.153.229:8983/solr/TEST_ACC/update?commit=true"
    final_data = []
    final_data = data
    try:
        result = requests.post(url=solr_url, data=json.dumps(final_data),
                          headers={'content-type': 'application/json'})
        if result.status_code == 200:
            print '\nDATA pushed to Solr'
        else:
            print "\nFailed to push data to solr"

    except Exception as ie:
        print "Exception occured" + str(ie)

def ConvertcsvTojson():

    inputfile = "/home/user/VolvoCore/scripts/AudetemiCSV/Business_Address_data.csv"
    outputfile = os.path.splitext(inputfile)[0] + "_modified.csv"
    jsonfile = ""
    with open(inputfile, 'rb') as inFile, open(outputfile, 'wb') as outfile:
        r = csv.reader(inFile, delimiter='|')
        w = csv.writer(outfile, delimiter='|')
        headers = next(r)
        solr_header = [solrdata.get(header) for header in headers]

        if len(solr_header) != len(headers):
            print "Data Dump failed because of headers"
            return False
        w.writerow(solr_header)

        for row in r:
            w.writerow(row)

    for filename in glob.glob(outputfile):
        csvfile = os.path.splitext(filename)[0]

        # '/home/user/VolvoCore/scripts/AudetemiCSV/Business_Address_data_modified'

        jsonfile = csvfile + '.json'

        # '/home/user/VolvoCore/scripts/AudetemiCSV/Business_Address_data_modified.json

        accountaddr_csvfile = "/home/user/VolvoCore/scripts/AudetemiCSV/Account_Address_data.csv"

        with open(csvfile + '.csv') as f:
            reader = csv.DictReader(f, delimiter='|')
            rows = list(reader)

        with open(accountaddr_csvfile) as f:
            # < openfile'/home/user/VolvoCore/scripts/AudetemiCSV/Business_Address_data_modified.csv', mode'r'at0x7f2abe65ec00 >

            reader = csv.DictReader(f, delimiter='|')


        with open(jsonfile, 'w') as f:
            # < openfile'/home/user/VolvoCore/scripts/AudetemiCSV/Business_Address_data_modified.json', mode'w'at0x7f2abe65ec00 >

            json.dump(rows, f)

    data = json.load(open(jsonfile))

    os.remove(outputfile)
    os.remove(jsonfile)
    return data


if __name__ == '__main__':
    try:

        data = ConvertcsvTojson()
        push_data_to_solr(data)
    except Exception as ae:
         msg = "Exception: " + str(ae)
