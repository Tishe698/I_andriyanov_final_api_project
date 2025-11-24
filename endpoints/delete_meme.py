import requests


from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    def full_req_delete_meme(self, post_id, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/meme/{post_id}',
            headers=headers,
        )
        return self.response