import requests
import allure  # для красивых шагов в отчёте

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

    @allure.step("Check that token exists and not empty")  # шаг в Allure-отчёте
    def check_token_not_empty(self):
        # проверяем что поле token вообще есть в ответе
        assert "token" in self.json, "Response doesn't contain 'token' field"
        # проверяем что токен не пустая строка
        assert self.json["token"] != "", "Token is empty"
