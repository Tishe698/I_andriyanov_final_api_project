import allure


payload_for_token = {
    "name": "ivan_andriyanov2.0",
}


@allure.feature("get token")
@allure.story("Получение токена авторизации")
def test_get_token(fixt_get_token):
    fixt_get_token.full_req_get_authorization_token(payload_for_token)  # запрос токена
    with allure.step("Проверяем что запрос прошёл успешно и вернулся статус 200"):
        fixt_get_token.check_status_code_is_200()
    with allure.step("Проверяем что в ответе есть поле token и оно не пустое"):
        json_response = fixt_get_token.json
        assert "token" in json_response  # поле token должно быть в ответе
        with allure.step("Проверяем что токен не пустой"):
            assert json_response["token"] != ""  # токен не должен быть пустой строкой
    with allure.step("Проверяем что при неверном формате запроса возвращается 400"):
        bad_payload = {"wrong_field": 123}
        fixt_get_token.full_req_get_authorization_token(bad_payload)  # запрос с неверным телом
        assert fixt_get_token.response.status_code == 400  # ожидаем статус ошибки 400
