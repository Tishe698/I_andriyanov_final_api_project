import requests

from endpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    def full_req_get_one_meme(self,post_id, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url = f'{self.url}/meme/{post_id}',
            headers = headers
        )
        return self.response