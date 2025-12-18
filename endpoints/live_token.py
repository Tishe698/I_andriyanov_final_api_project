import requests

from endpoints.base_endpoint import BaseEndpoint


class LiveToken(BaseEndpoint):
    def full_req_live_token(self, headers={"Content-Type": "application/json"}):
        self.response = requests.get(
            f"{self.url}/authorize/{self._token}",  # GET запрос на /authorize/{token}
            headers=headers,
        )
        try:
            self.json = self.response.json()  # сохраняем json, если он есть
        except ValueError:
            self.json = None  # например, 404 с HTML
        return self.response
