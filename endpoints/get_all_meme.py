import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):
    def full_req_get_all_meme(self, headers=None):
        headers = headers if headers else self.headers  # можно переопределить заголовки
        self.response = requests.get(url=f"{self.url}/meme", headers=headers)  # GET список
        try:
            self.json = self.response.json()  # сохраняем тело ответа для проверок
        except ValueError:
            self.json = None  # например, 4xx с HTML
        return self.response
