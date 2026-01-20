import allure


# Позитивный тест: получение списка всех мемов
@allure.feature("get all meme")
@allure.story("Получение всех мемов")
def test_get_all_meme_success(fixt_get_all_meme):
    fixt_get_all_meme.full_req_get_all_meme()  # запрос списка всех мемов
    fixt_get_all_meme.check_status_code(200)  # проверяем статус 200
    fixt_get_all_meme.check_response_not_empty()  # проверяем что ответ не пустой


# Негативный тест: запрос с неверным токеном
@allure.feature("get all meme")
@allure.story("Ошибка при неверном токене")
def test_get_all_meme_unauthorized(fixt_get_all_meme):
    fixt_get_all_meme.full_req_get_all_meme(
        headers=fixt_get_all_meme.BAD_TOKEN_HEADERS
    )  # неверный токен
    fixt_get_all_meme.check_status_code(401)  # ожидаем ошибку 401
