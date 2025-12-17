import requests


from endpoints.base_endpoint import BaseEndpoint


class ChangePutMeme(BaseEndpoint):
    def full_req_change_put_meme(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers  # заголовки можно переопределить
        self.response = requests.put(
            f"{self.url}/meme/{post_id}", json=payload, headers=headers
        )  # PUT обновляет мем по id
        try:
            self.json = self.response.json()  # только если реально JSON
        except ValueError:
            self.json = None  # для 4xx с HTML

        return self.response
