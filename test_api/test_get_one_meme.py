import allure
from conftest import PAYLOAD  # исходные данные для создания мема в фикстуре


@allure.feature("get one meme")
@allure.story("Получение одного поста")
def test_get_one_meme(fixt_get_one_meme, fixt_get_post_id):
    post_id = fixt_get_post_id  # id мема создаётся фикстурой заранее (POST в fixt_get_post_id)
    fixt_get_one_meme.full_req_get_one_meme(post_id)  # первый запрос: читаем только что созданный мем
    with allure.step("Проверяем статус 200"):
        fixt_get_one_meme.check_status_code_is_200()  # убеждаемся, что GET вернул успешный код
    with allure.step("Проверяем, что полученный мем соответствует созданному"):
        json_response = fixt_get_one_meme.json  # тело ответа из последнего GET
        assert json_response["id"] == post_id  # id должен совпасть с созданным
        assert json_response["text"] == PAYLOAD["text"]  # поля должны совпасть с исходными данными
        assert json_response["url"] == PAYLOAD["url"]
        assert json_response["tags"] == PAYLOAD["tags"]
        assert json_response["info"] == PAYLOAD["info"]
    with allure.step("Проверяем, что при запросе несуществующего мема возвращается 404"):
        fixt_get_one_meme.full_req_get_one_meme(9999999)  # второй запрос: заведомо несуществующий id
        assert fixt_get_one_meme.response.status_code == 404  # ожидаем корректный статус ошибки
