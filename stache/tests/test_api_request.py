import unittest
import json

from stache import api_request
from stache.tests.get_credentials_for_tests import get_config

config = get_config()

class TestSpiRequest(unittest.TestCase):

    def test_retrieve_creds(self):

        expected_list = [config.isu_purpose,
                         config.isu_secret,
                         config.isu_nickname,
                         config.isu_memo]


        purpose, secret, nickname, memo = api_request.retrieve_creds(config.isu_api_key,
                                                              str(config.isu_item_id))
        result_list = [purpose, secret, nickname, memo]

        self.assertEqual(result_list, expected_list)


    def test_parse_response(self):
        data = ({'nickname': config.isu_nickname, 'secret': config.isu_secret})
        response = json.dumps(data.encode('utf-8'))

        nickname, password = api_request.parse_response(response)

        self.assertEqual([nickname, password], [config.isu_nickname,
                                                 config.isu_secret])