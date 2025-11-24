import allure

from conftest import PAYLOAD_CHANGE

DATA = PAYLOAD_CHANGE


@allure.feature('change meme put')
@allure.story('Изменение мема Put')
def test_change_put_meme(fixt_change_put_meme, fixt_get_post_id):
    fixt_change_put_meme.full_req_change_put_meme(fixt_get_post_id, payload = DATA)
    with allure.step('Обновляем существующий мем через PUT и ожидаем 200'):
        assert fixt_change_put_meme.check_status_code_is_200
