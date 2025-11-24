import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateNewMeme(BaseEndpoint):
    post_id = None

    def full_req_create_new_meme(self,payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url = f'{self.url}/meme',
            headers = headers,
            json = payload
        )
        self.json = self.response.json()
        self.post_id = self.json["id"]
        return self.response