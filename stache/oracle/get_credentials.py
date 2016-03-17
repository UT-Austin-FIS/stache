from stache import api_request


class GetOracleCredentials(object):
    def __init__(self, api_key, item_id, env):

        self.api_key = api_key
        self.item_id = item_id
        self.env = env

    def ret_creds(self):
        (purpose,
         secret,
         nickname,
         memo) = api_request.retrieve_creds(self.api_key,
                                            self.item_id)
        password = self.parse_secret(secret)

        return nickname, password

    def parse_secret(self, secret):
        '''
        Parse out secret to only return requested environment.
        Expected Format in Secret:

        DEV: dev-password
        QUAL: qual-password
        PROD: prod-password

        '''
        list = [x.strip() for x in secret.split('\n')]

        secret_dict = {}
        for y in list:
            piece = [x.strip() for x in y.split(':')]
            secret_dict[piece[0]] = piece[1]

        password = secret_dict[self.env]
        return password
