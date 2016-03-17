import unittest

from stache.all_fields.get_stache_entry import GetStacheEntry
from stache.tests.get_credentials_for_tests import get_config

config = get_config()


class TestGetStacheEntry(unittest.TestCase):

    def test_return_fields(self):

        expected_list = [config.isu_purpose,
                         config.isu_secret,
                         config.isu_nickname,
                         config.isu_memo]

        reference = GetStacheEntry(config.isu_api_key,
                                   str(config.isu_item_id))
        purpose, secret, nickname, memo = reference.return_fields()

        result_list = [purpose, secret, nickname, memo]

        print('\n')
        print("This test will fail until bug is fixed in stache API.")

        self.assertEqual(result_list, expected_list)
