import allure

@allure.feature('get one meme')
@allure.story('Получение одного поста')
def test_get_one_meme(fixt_get_one_meme, fixt_get_post_id):
    fixt_get_one_meme.full_req_get_one_meme(fixt_get_post_id)
    with allure.step('Получаем конкретный мем и проверяем статус 200'):
        assert fixt_get_one_meme.check_status_code_is_200
