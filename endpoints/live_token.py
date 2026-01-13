import requests
import allure  # для красивых шагов в отчёте

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

    @allure.step("Check that token is alive message present")  # шаг в Allure-отчёте
    def check_token_is_alive_message(self):
        # проверяем что в ответе есть сообщение о живом токене
        assert (
            "Token is alive. Username is" in self.response.text
        ), f"Expected 'Token is alive' message, got: {self.response.text}"
