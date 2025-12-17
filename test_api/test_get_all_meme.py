import allure


@allure.feature("get all meme")
@allure.story("Получение всех постов")
def test_get_all_meme(fixt_get_all_meme):
    fixt_get_all_meme.full_req_get_all_meme()  # запрос списка всех мемов
    with allure.step("Запрашиваем список мемов и убеждаемся в статусе 200"):
        fixt_get_all_meme.check_status_code_is_200()
    with allure.step("Проверяем что токен не верный"):
        fixt_get_all_meme.full_req_get_all_meme(headers={"Authorization": "BadToken"})
        assert fixt_get_all_meme.response.status_code == 401
