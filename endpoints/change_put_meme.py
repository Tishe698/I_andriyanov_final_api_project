import requests


from endpoints.base_endpoint import BaseEndpoint


class ChangePutMeme(BaseEndpoint):
    def full_req_change_put_meme(self, post_id, payload, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/meme/{post_id}',
            json=payload,
            headers=headers
        )
        return self.response