import allure


payload_for_token = {
    "name": "ivan_andriyanov2.0",
}


# Позитивный тест: правильный запрос → получаем токен
@allure.feature("get token")
@allure.story("Получение токена авторизации")
def test_get_token_success(fixt_get_token):
    fixt_get_token.full_req_get_authorization_token(payload_for_token)  # запрос токена
    fixt_get_token.check_status_code(200)  # проверяем статус 200
    fixt_get_token.check_token_not_empty()  # проверяем что токен есть и не пустой


# Негативный тест: кривой payload → ошибка 400
@allure.feature("get token")
@allure.story("Ошибка при неверном payload")
def test_get_token_bad_payload(fixt_get_token):
    bad_payload = {"wrong_field": 123}  # неправильные данные
    fixt_get_token.full_req_get_authorization_token(
        bad_payload
    )  # запрос с неверным телом
    fixt_get_token.check_status_code(400)  # ожидаем ошибку 400
