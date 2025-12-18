import requests


from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    def full_req_delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers  # можно пробросить свои заголовки
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=headers,
        )  # удаляем конкретный мем
        return self.response
