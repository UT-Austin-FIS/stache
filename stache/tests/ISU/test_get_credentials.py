import unittest

from stache.ISU.get_credentials import GetISUCredentials
from stache.tests.get_credentials_for_tests import get_config

config = get_config()


class TestGetISUCredentials(unittest.TestCase):

    def test_process_reasons(self):

        reference = GetISUCredentials(config.isu_api_key,
                                      str(config.isu_item_id))

        nickname, password = reference.ret_creds()

        self.assertEqual([nickname, password], [config.isu_nickname,
                                                 config.isu_secret])
