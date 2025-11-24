import allure

@allure.feature('delete one meme')
@allure.story('Удаление одного поста')
def test_delete_meme(fixt_delete_meme, fixt_get_post_id):
    fixt_delete_meme.full_req_delete_meme(fixt_get_post_id)
    with allure.step('Удаляем созданный мем и ожидаем статус 200'):
        assert fixt_delete_meme.check_status_code_is_200
