import requests
import allure


class BaseEndpoint:
    # Базовый URL твоего API (общий для всех запросов)
    url = "http://memesapi.course.qa-practice.com"

    # Заголовки с невалидным токеном — для тестов на 401
    BAD_TOKEN_HEADERS = {"Authorization": "BadToken"}

    # Сюда каждый эндпоинт будет класть результат последнего запроса
    response = None  # объект requests.Response
    json = None  # распарсенный response.json()

    # ВАЖНО:
    # Это атрибут КЛАССА (общий для всех экземпляров BaseEndpoint и его наследников).
    # Он живёт "в памяти процесса Python", то есть:
    # - один раз на весь прогон pytest (пока pytest не завершится)
    # - после перезапуска pytest снова станет None и токен снова запросится
    _token = None

    def __init__(self):
        """
        __init__ вызывается каждый раз, когда ты создаёшь объект эндпоинта:
        CreateNewMeme(), GetOneMeme(), DeleteMeme() и т.д.

        Наша цель:
        - иметь ОДИН токен на весь прогон
        - если токена нет или он умер — получить новый
        - собрать self.headers для запросов
        """

        # 1) Если токен ещё не получали вообще (первый эндпоинт в прогоне)
        if BaseEndpoint._token is None:
            BaseEndpoint._token = self._get_new_token()

        # 2) Если токен уже есть, но мог протухнуть — проверяем и обновляем
        #    (например, токены живут 5 минут, а тесты идут 15 минут)
        elif not self._is_token_valid(BaseEndpoint._token):
            BaseEndpoint._token = self._get_new_token()

        # 3) На основе общего токена собираем заголовки для КОНКРЕТНОГО объекта
        #    (headers уже обычный атрибут экземпляра)
        self.headers = {
            "content-type": "application/json",
            "authorization": BaseEndpoint._token,
        }

    def _is_token_valid(self, token: str) -> bool:
        """
        Проверяем, живой ли токен.
        API возвращает 200, если токен валиден.
        """
        r = requests.get(f"{self.url}/authorize/{token}")
        return r.status_code == 200

    def _get_new_token(self) -> str:
        """
        Запрашиваем новый токен.
        """
        r = requests.post(
            url=f"{self.url}/authorize",
            json={"name": "ivan_andriyanov"},
            headers={"content-type": "application/json"},
        )

        # На случай если API сломалось — лучше упасть здесь с понятной причиной
        assert r.status_code == 200, f"Auth failed: {r.status_code}, body={r.text}"

        # ВАЖНО: ключ должен совпадать с тем, что реально возвращает API
        return r.json()["token"]

    @allure.step("check status code is {expected_code}")
    def check_status_code(self, expected_code: int):
        assert (
            self.response.status_code == expected_code
        ), f"Expected {expected_code}, got {self.response.status_code}"

    @allure.step("Check that response data matches sent payload")  # шаг в Allure-отчёте
    def check_response_matches_payload(self, payload):
        # проверяем что каждое поле в ответе совпадает с тем, что отправили
        assert self.json["text"] == payload["text"], "text doesn't match"
        assert self.json["url"] == payload["url"], "url doesn't match"
        assert self.json["tags"] == payload["tags"], "tags doesn't match"
        assert self.json["info"] == payload["info"], "info doesn't match"
