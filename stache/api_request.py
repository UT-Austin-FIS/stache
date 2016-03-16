import json
import requests


class ISUError(Exception):
    pass


URL = "https://stache.utexas.edu/api/v1/item/read/"

def retrieve_creds(api_key, item_id):
    url = URL + item_id
    headers = {'X-STACHE-READ-KEY': api_key}
    response = requests.get(url, headers=headers)

    if response.ok:
        return parse_response(response)
    else:
        response.raise_for_status()


def parse_response(response):
    jData = json.loads(response.content.decode('utf-8'))

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key + " : " + jData[key])

    return(jData['purpose'],
           jData['secret'],
           jData['nickname'],
           jData['memo'],
           )