import requests

from endpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    def full_req_get_one_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers  # можно задать кастомные заголовки
        self.response = requests.get(f"{self.url}/meme/{meme_id}", headers=headers)  # GET по id
        try:
            self.json = self.response.json()  # сохраняем json, если он есть
        except ValueError:
            self.json = None  # например, 404 с HTML
        return self.response
