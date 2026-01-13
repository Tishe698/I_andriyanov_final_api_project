import allure


# Позитивный тест: валидный токен → токен жив
@allure.feature("is alive token")
@allure.story("Проверка жив ли токен авторизации")
def test_is_alive_token_success(fixt_is_alive_token):
    fixt_is_alive_token.full_req_live_token()  # запрос проверки токена
    fixt_is_alive_token.check_status_code(200)  # проверяем статус 200
    fixt_is_alive_token.check_token_is_alive_message()  # проверяем сообщение о живом токене


# Негативный тест: невалидный токен → ошибка 404
@allure.feature("is alive token")
@allure.story("Ошибка при неверном токене")
def test_is_alive_token_invalid(fixt_is_alive_token):
    fixt_is_alive_token._token = (
        "A6RzAY3M4o12345"  # подменяем токен на заведомо неверный
    )
    fixt_is_alive_token.full_req_live_token()  # запрос с неверным токеном
    fixt_is_alive_token.check_status_code(404)  # сервер должен вернуть 404
