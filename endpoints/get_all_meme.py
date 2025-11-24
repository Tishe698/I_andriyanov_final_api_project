import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):
    def full_req_get_all_meme(self, headers = None):
        headers = headers if headers else self.headers
        self.response  = requests.get(
            url = f'{self.url}/meme',
            headers=headers
        )
        return self.response