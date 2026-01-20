import allure
import pytest

from payload import PAYLOAD, BADDATA, GOODDATA

# Позитивный тест: создание мема с валидными данными
@allure.feature("create meme")
@allure.story("Создание мема")
@pytest.mark.parametrize("data", GOODDATA)
def test_create_new_meme_success(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(payload=data)  # создаём новый мем
    fix_create_new_meme.check_status_code(200)  # проверяем статус 200
    fix_create_new_meme.check_response_matches_payload(
        data
    )  # проверяем что ответ совпадает с payload


# Негативный тест: создание мема с невалидными данными
@allure.feature("create meme")
@allure.story("Ошибка при создании мема с невалидными данными")
@pytest.mark.parametrize("data", BADDATA)
def test_create_new_meme_bad_body(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(payload=data)  # запрос с невалидными данными
    fix_create_new_meme.check_status_code(400)  # ожидаем ошибку 400



# Негативный тест: создание мема без авторизации
@allure.feature("create meme")
@allure.story("Ошибка при создании мема без токена")
def test_create_new_meme_unauthorized(fix_create_new_meme):
    fix_create_new_meme.full_req_create_new_meme(
        payload=PAYLOAD, headers=fix_create_new_meme.BAD_TOKEN_HEADERS  # неверный токен
    )
    fix_create_new_meme.check_status_code(401)  # ожидаем ошибку 401
