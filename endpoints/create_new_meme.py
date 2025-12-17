import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateNewMeme(BaseEndpoint):
    post_id = None  # id последнего созданного мема

    def full_req_create_new_meme(self, payload, headers=None):
        headers = headers if headers else self.headers  # можно переопределить заголовки
        self.response = requests.post(
            url=f"{self.url}/meme", headers=headers, json=payload
        )  # создаём мем
        try:
            self.json = self.response.json()  # сохраняем тело ответа
            self.post_id = self.json["id"]  # и id созданного мема
        except ValueError:
            self.json = None  # например, 4xx с HTML
            return self.response
