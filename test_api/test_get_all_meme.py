import allure

@allure.feature('get all meme')
@allure.story('Получение всех постов')
def test_get_all_meme(fixt_get_all_meme):
    fixt_get_all_meme.full_req_get_all_meme()
    with allure.step('Запрашиваем список мемов и убеждаемся в статусе 200'):
        assert fixt_get_all_meme.check_status_code_is_200
