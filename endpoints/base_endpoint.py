import requests
import allure


class BaseEndpoint:
    # Базовые поля и общий URL API
    url = "http://memesapi.course.qa-practice.com"
    response = None  # хранит последний объект Response
    json = None  # хранит распарсенный json последнего ответа
    _token = None  # кэш токена авторизации между экземплярами

    def __init__(self):
        # Если токена нет или токен невалидный — получаем новый
        if not self._token or not self.is_token_valid():
            self._token = self.get_new_token()
        self.headers = {
            "content-type": "application/json",
            "authorization": self._token,
        }  # общие заголовки для всех запросов

    def is_token_valid(self):
        response = requests.get(url=f"{self.url}/authorize/{self._token}")
        return response.status_code == 200  # API возвращает 200, если токен жив

    def get_new_token(self):
        # Запрашиваем новый токен на имя пользователя
        response = requests.post(
            url=f"{self.url}/authorize",
            json={"name": "ivan_andriyanov"},
            headers={"content-type": "application/json"},
        )
        token = response.json()["token"]
        return token

    @allure.step("Check that response is 200")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200  # базовая проверка успешного ответа
