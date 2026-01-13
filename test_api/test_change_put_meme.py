import allure
import copy


# Позитивный тест: изменение мема с валидными данными
@allure.feature("change meme put")
@allure.story("Изменение мема Put")
def test_change_put_meme_success(
    fixt_change_put_meme, fixt_get_meme_id, fixt_payload_change
):
    meme_id = fixt_get_meme_id  # id мема, созданного фикстурой
    payload = copy.deepcopy(fixt_payload_change)  # чистая копия исходных данных
    payload["id"] = meme_id  # API требует id в теле
    fixt_change_put_meme.full_req_change_put_meme(meme_id, payload)  # изменяем мем
    fixt_change_put_meme.check_status_code(200)  # проверяем статус 200
    fixt_change_put_meme.check_response_matches_payload(
        payload
    )  # проверяем что ответ совпадает с payload


# Негативный тест: изменение мема с неверным типом поля
@allure.feature("change meme put")
@allure.story("Ошибка при неверном типе поля")
def test_change_put_meme_invalid_field(
    fixt_change_put_meme, fixt_get_meme_id, fixt_payload_change
):
    meme_id = fixt_get_meme_id  # id мема, созданного фикстурой
    payload = copy.deepcopy(fixt_payload_change)  # чистая копия исходных данных
    payload["id"] = meme_id  # API требует id в теле
    payload["text"] = 12345  # заведомо неверный тип поля
    fixt_change_put_meme.full_req_change_put_meme(
        meme_id, payload
    )  # запрос с неверным типом
    fixt_change_put_meme.check_status_code(400)  # ожидаем ошибку 400


# Негативный тест: изменение мема без авторизации
@allure.feature("change meme put")
@allure.story("Ошибка при изменении мема без токена")
def test_change_put_meme_unauthorized(
    fixt_change_put_meme, fixt_get_meme_id, fixt_payload_change
):
    meme_id = fixt_get_meme_id  # id мема, созданного фикстурой
    payload = copy.deepcopy(fixt_payload_change)
    payload["id"] = meme_id
    fixt_change_put_meme.full_req_change_put_meme(
        meme_id,
        payload,
        headers=fixt_change_put_meme.BAD_TOKEN_HEADERS,  # неверный токен
    )
    fixt_change_put_meme.check_status_code(401)  # ожидаем ошибку 401
