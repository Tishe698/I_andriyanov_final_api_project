import allure
from payload import PAYLOAD  # исходные данные для создания мема в фикстуре


# Позитивный тест: получение существующего мема
@allure.feature("get one meme")
@allure.story("Получение одного мема")
def test_get_one_meme_success(fixt_get_one_meme, fixt_get_meme_id):
    meme_id = fixt_get_meme_id  # id мема создаётся фикстурой заранее
    fixt_get_one_meme.full_req_get_one_meme(meme_id)  # запрос мема по id
    fixt_get_one_meme.check_status_code(200)  # проверяем статус 200
    fixt_get_one_meme.check_response_matches_payload(
        PAYLOAD
    )  # проверяем что данные совпадают


# Негативный тест: получение несуществующего мема
@allure.feature("get one meme")
@allure.story("Ошибка при запросе несуществующего мема")
def test_get_one_meme_not_found(fixt_get_one_meme):
    fixt_get_one_meme.full_req_get_one_meme(9999999)  # заведомо несуществующий id
    fixt_get_one_meme.check_status_code(404)  # ожидаем ошибку 404


# Негативный тест: получение мема без авторизации
@allure.feature("get one meme")
@allure.story("Ошибка при запросе мема без токена")
def test_get_one_meme_unauthorized(fixt_get_one_meme, fixt_get_meme_id):
    meme_id = fixt_get_meme_id  # id мема из фикстуры
    fixt_get_one_meme.full_req_get_one_meme(
        meme_id, headers=fixt_get_one_meme.BAD_TOKEN_HEADERS  # неверный токен
    )
    fixt_get_one_meme.check_status_code(401)  # ожидаем ошибку 401
