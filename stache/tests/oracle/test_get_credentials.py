import functools
import os
import sys
import unittest
from collections import namedtuple

from stache.oracle.get_credentials import GetOracleCredentials

Configuration = namedtuple('Config', ('isu_api_key',
                                      'isu_item_id',
                                      'isu_nickname',
                                      'isu_secret',
                                      'oracle_api_key',
                                      'oracle_item_id',
                                      'oracle_nickname',
                                      'oracle_dev_secret',))

def find_config():
    first_print = functools.partial(print, '\n\n')
    def nop(**kwargs):
        pass

    def separate_on_console(**kwargs):
        nonlocal first_print
        first_print(**kwargs)
        first_print = nop

    def message(msg, **kwargs):
        separate_on_console(**kwargs)
        print(msg, **kwargs)

    try:
        import yaml
    except ImportError:
        message('PyYAML must be installed to run tests.',
                file=sys.stderr
        )
        return None

    config_path = os.environ.get('STACHE_TEST_CONFIG')
    message('>> STACHE_TEST_CONFIG: ' + str(config_path or ''))
    if config_path and not os.path.exists(config_path):
        message('Unable to use the configuration path '
                'specified in the environment variable '
                'STACHE_TEST_CONFIG'
        )
        return None # we bail if you specified a path that doesn't exist

    if config_path is None:
        config_path = os.path.join(os.getcwd(), 'test_config.yaml')
        if not os.path.exists(config_path):
            config_path = ''
            while not os.path.exists(config_path):
                if config_path != '':
                    print('> "{0}" is not a valid path.'.format(config_path),
                          file=sys.stderr)

                separate_on_console()
                config_path = input('Enter a test config path or enter for no ')
                if config_path == '':
                    break

    if config_path == '':
        return None
    else:
        with open(config_path, 'r') as f:
            config = yaml.load(f)
            separate_on_console()
            print('> Using Configuration file at "{0}"\n'.format(config_path))
            return Configuration(config['isu_api_key'],
                                 config['isu_item_id'],
                                 config['isu_nickname'],
                                 config['isu_secret'],
                                 config['oracle_api_key'],
                                 config['oracle_item_id'],
                                 config['oracle_nickname'],
                                 config['oracle_dev_secret'],)

def get_config():
    config = find_config()
    if config:
        return config
    else:
        return None

config = get_config()

class TestGetOracleCredentials(unittest.TestCase):

    def test_ret_creds(self):

        reference = GetOracleCredentials(config.oracle_api_key,
                                         config.oracle_item_id,
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
        password = reference.parse_secret(secret, env)

        self.assertEqual(password, "qual-password")
