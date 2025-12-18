import allure
import copy


@allure.feature("change meme put")
@allure.story("Изменение мема Put")
def test_change_put_meme(fixt_change_put_meme, fixt_get_meme_id, fixt_payload_change):
    meme_id = fixt_get_meme_id  # id мема, созданного фикстурой
    payload = copy.deepcopy(fixt_payload_change)  # чистая копия исходных данных
    payload["id"] = meme_id  # API требует id в теле
    fixt_change_put_meme.full_req_change_put_meme(meme_id, payload)
    with allure.step("Изменяем созданный мем и убеждаемся, что ответ 200"):
        fixt_change_put_meme.check_status_code_is_200()
    with allure.step("Проверяем, что изменения сохранились"):
        json_response = fixt_change_put_meme.json
        # почему-то id приходит как строка
        assert fixt_change_put_meme.json["id"] == str(meme_id)
        assert json_response["text"] == payload["text"]
        assert json_response["url"] == payload["url"]
        assert json_response["tags"] == payload["tags"]
        assert json_response["info"] == payload["info"]
    with allure.step("Проверяем, если передан неверный формат поля"):
        payload["text"] = 12345  # заведомо неверный тип поля для негативного кейса
        fixt_change_put_meme.full_req_change_put_meme(meme_id, payload)  # ожидаем 400
        assert fixt_change_put_meme.response.status_code == 400
