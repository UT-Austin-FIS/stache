import api_request


class GetISUCredentials(object):
    def __init__(self, api_key, item_id):

        self.api_key = api_key
        self.item_id = item_id


    def ret_creds(self):
        purpose,secret, nickname, memo = api_request.retrieve_creds(self.api_key,
                                                                     self.item_id)
        return nickname, secret

