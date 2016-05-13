from stache import api_request


class GetCredential(object):
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
        Environment is just the key of the dictionary in stache.
        Expected Format in Secret:

        env: password123
        env: passwordABC

        '''
        list_envs = [x.strip() for x in secret.split('\n')]

        secret_dict = {}
        for y in list_envs:
            piece = [x.strip() for x in y.split(':')]
            secret_dict[piece[0]] = piece[1]

        password = secret_dict[self.env]
        return password
