import requests
from requests import ConnectionError, Response
from rest_framework import status




def get_solr_data(url):
    response_data = []
    try:
        response_data = requests.get(url)


    except ConnectionError as ce:
        return Response(status=status.HTTP_412_PRECONDITION_FAILED)

    if response_data.status_code == 200:
        response_data_json = response_data.json()
        response_data = response_data_json.get("response", {}).get("docs", [])

    return response_data
