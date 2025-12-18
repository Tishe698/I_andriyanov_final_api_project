import allure


@allure.feature("is alive token")
@allure.story("Проверка жив ли токен авторизации")
def test_is_alive_token(fixt_is_alive_token):
    fixt_is_alive_token.full_req_live_token()  # запрос проверки токена
    with allure.step("Проверяем что запрос прошёл успешно и вернулся статус 200"):
        fixt_is_alive_token.check_status_code_is_200()
    with allure.step("Проверяем что в ответе есть сообщение : Token is alive. Username is"):
        assert "Token is alive. Username is" in fixt_is_alive_token.response.text
    with allure.step("Проверяем что при неверном токене возвращается 404"):
        fixt_is_alive_token._token = "A6RzAY3M4o12345"  # подменяем токен на заведомо неверный
        fixt_is_alive_token.full_req_live_token()  # аргументы не передаём!
        assert fixt_is_alive_token.response.status_code == 404  # сервер должен вернуть 404
