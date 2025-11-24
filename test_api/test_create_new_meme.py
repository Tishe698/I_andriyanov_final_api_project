import allure
import pytest

from conftest import PAYLOAD

DATA = [PAYLOAD]



@allure.feature('creaete meme')
@allure.story('Создание поста мема')
@pytest.mark.parametrize('data', DATA)
def test_create_new_meme(fix_create_new_meme, data):
    fix_create_new_meme.full_req_create_new_meme(payload=data)
    with allure.step('Создаём новый мем и убеждаемся, что ответ 200'):
        assert fix_create_new_meme.check_status_code_is_200
