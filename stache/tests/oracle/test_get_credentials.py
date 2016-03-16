import unittest

from stache.oracle.get_credentials import GetOracleCredentials
from stache.tests.get_credentials_for_tests import get_config

config = get_config()

class TestGetOracleCredentials(unittest.TestCase):

    def test_ret_creds(self):

        reference = GetOracleCredentials(config.oracle_api_key,
                                         str(config.oracle_item_id),
                                         "DEV")
        nickname, password = reference.ret_creds()

        self.assertEqual([nickname, password], [config.oracle_nickname,
                                                 config.oracle_dev_secret])


    def test_parse_secret(self):

        secret = "DEV: dev-password\nQUAL: qual-password\nPROD: prod-password"
        env = "QUAL"

        reference = GetOracleCredentials(config.oracle_api_key,
                                         config.oracle_item_id,
                                         env)
        password = reference.parse_secret(secret)

        self.assertEqual(password, "qual-password")
