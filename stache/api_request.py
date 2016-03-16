import json
import requests
import time


class ISUError(Exception):
    pass


URL = "https://stache.utexas.edu/api/v1/item/read/"

def retrieve_creds(api_key, item_id):
    url = URL + item_id
    headers = {'X-STACHE-READ-KEY': api_key}
    response = requests.get(url, headers=headers)

    if response.ok:
        return parse_response(response.content)
    elif response.status_code == 429:
        time.sleep(5)  # request limited to once every 5 seconds, try once
        response = requests.get(url, headers=headers) # more before failing
        if response.ok:
            return parse_response(response.content)
        else:
            response.raise_for_status()
    else:
        response.raise_for_status()



def parse_response(response):
    jData = json.loads(response.decode('utf-8'))

    return(jData['purpose'],
           jData['secret'],
           jData['nickname'],
           jData['memo'],
           )