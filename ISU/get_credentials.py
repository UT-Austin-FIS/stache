import requests
import json

# todo: fix
from _local_settings import API_KEY, ITEM_ID, URL


class ISUError(Exception):
    pass


class ISU(object):
    def __init__(self, api_key, item_id):

        if api_key:
            self.api_key = api_key
        else:
            self.api_key = API_KEY

        if item_id:
            self.item_id = item_id
        else:
            self.item_id = ITEM_ID


    def ret_creds(self):
        # todo: this should really use API key in header
        url = URL + "{0}/?key={1}".format(self.item_id, self.api_key)
        print(url)

        # data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
        response = requests.get(url)

        if response.ok:
            username, password = self.parse_response(response)

        else:
        # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()

        return username, password


    def parse_response(self, response):
        jData = json.loads(response.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        for key in jData:
            print(key + " : " + jData[key])

        return(jData['nickname'], jData['secret'])

