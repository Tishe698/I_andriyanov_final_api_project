import allure


@allure.feature("delete one meme")
@allure.story("Удаление одного мема")
def test_delete_meme(fixt_delete_meme, fixt_get_meme_id, fixt_get_one_meme):
    meme_id = fixt_get_meme_id  # id мема из фикстуры (создан заранее)
    fixt_delete_meme.full_req_delete_meme(meme_id)  # удаляем мем
    with allure.step("Удаляем созданный мем и ожидаем статус 200"):
        fixt_delete_meme.check_status_code_is_200()
    with allure.step("Проверяем что данного мема нет"):
        fixt_get_one_meme.full_req_get_one_meme(meme_id)  # повторный GET должен вернуть 404
        assert fixt_get_one_meme.response.status_code == 404  # мем после удаления недоступен
    with allure.step("Проверяем что повторное удаление данного мема возвращает 404"):
        fixt_delete_meme.full_req_delete_meme(meme_id)
        assert fixt_delete_meme.response.status_code == 404
    with allure.step("Проверяем что удаление мема с несуществующим id возвращает 404"):
        fixt_delete_meme.full_req_delete_meme(9999999)
        assert fixt_delete_meme.response.status_code == 404
