import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAuthorizationToken(BaseEndpoint):
    def full_req_get_authorization_token(
        self, payload, headers={"Content-Type": "application/json"}
    ):
        self.response = requests.post(
            f"{self.url}/authorize",
            json=payload,
            headers=headers,
        )
        try:
            self.json = self.response.json()  # сохраняем тело ответа
        except ValueError:
            self.json = None  # для 400 ошибок None
        return self.response
