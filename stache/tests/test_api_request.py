import unittest
import json
import requests

from stache import api_request
from stache.tests.get_credentials_for_tests import get_config

config = get_config()

class TestApiRequest(unittest.TestCase):

    def test_retrieve_creds(self):

        expected_list = [config.isu_purpose,
                         config.isu_secret,
                         config.isu_nickname,
                         config.isu_memo]


        purpose, secret, nickname, memo = api_request.retrieve_creds(config.isu_api_key,
                                                              str(config.isu_item_id))
        result_list = [purpose, secret, nickname, memo]

        print('\n')
        print("This test will fail until a bug where memo=purpose is fixed by stache")

        self.assertEqual(result_list, expected_list)


    def test_parse_response(self):
        data = ({'purpose': 'test1',
                 'secret': 'blah',
                 'nickname': 'bert',
                 'memo': 'memo memo'})
        expected_list = ['test1',
                         'blah',
                         'bert',
                         'memo memo']
        response = json.dumps(data)

        purpose, secret, nickname, memo = api_request.parse_response(response.encode('utf-8'))

        result_list = [purpose, secret, nickname, memo]

        self.assertEqual(result_list, expected_list)