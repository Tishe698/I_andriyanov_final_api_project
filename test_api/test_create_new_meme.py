import allure
import pytest
import copy

from conftest import PAYLOAD

DATA = [PAYLOAD]


@allure.feature("creaete meme")
@allure.story("Создание мема")
@pytest.mark.parametrize("data", DATA)
def test_create_new_meme(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(payload=data)  # создаём новый мем по базовому payload
    with allure.step("Создаём новый мем и убеждаемся, что ответ 200"):
        fix_create_new_meme.check_status_code_is_200()
    with allure.step("Проверяем, что созданный мем соответствует отправленным данным"):
        assert fix_create_new_meme.json["text"] == data["text"]
        assert fix_create_new_meme.json["url"] == data["url"]
        assert fix_create_new_meme.json["tags"] == data["tags"]
        assert fix_create_new_meme.json["info"] == data["info"]
    with allure.step("Проверяем, что при создании мема без обязательного поля возвращается 400"):
        bad_data = copy.deepcopy(data)  # отдельная копия для негативного запроса
        bad_data["url"] = None  # удаляем обязательное поле url
        fix_create_new_meme.full_req_create_new_meme(payload=bad_data)  # негативный запрос без url
        assert fix_create_new_meme.response.status_code == 400
