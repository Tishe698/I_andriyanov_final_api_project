import allure
import pytest
import copy

from conftest import PAYLOAD

DATA = [PAYLOAD]


# Позитивный тест: создание мема с валидными данными
@allure.feature("create meme")
@allure.story("Создание мема")
@pytest.mark.parametrize("data", DATA)
def test_create_new_meme_success(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(payload=data)  # создаём новый мем
    fix_create_new_meme.check_status_code(200)  # проверяем статус 200
    fix_create_new_meme.check_response_matches_payload(
        data
    )  # проверяем что ответ совпадает с payload


# Негативный тест: создание мема без обязательного поля url
@allure.feature("create meme")
@allure.story("Ошибка при создании мема без url")
@pytest.mark.parametrize("data", DATA)
def test_create_new_meme_without_url(fix_create_new_meme, data):
    bad_data = copy.deepcopy(data)  # отдельная копия для негативного запроса
    bad_data["url"] = None  # удаляем обязательное поле url
    fix_create_new_meme.full_req_create_new_meme(payload=bad_data)  # запрос без url
    fix_create_new_meme.check_status_code(400)  # ожидаем ошибку 400


# Негативный тест: создание мема без авторизации
@allure.feature("create meme")
@allure.story("Ошибка при создании мема без токена")
@pytest.mark.parametrize("data", DATA)
def test_create_new_meme_unauthorized(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(
        payload=data, headers=fix_create_new_meme.BAD_TOKEN_HEADERS  # неверный токен
    )
    fix_create_new_meme.check_status_code(401)  # ожидаем ошибку 401
