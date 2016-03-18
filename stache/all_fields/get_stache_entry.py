from stache import api_request


class GetStacheEntry(object):
    def __init__(self, api_key, item_id):

        self.api_key = api_key
        self.item_id = item_id

    def return_fields(self):
        '''Return purpose,secret, nickname, memo from stache entry.'''

        return api_request.retrieve_creds(self.api_key, self.item_id)
