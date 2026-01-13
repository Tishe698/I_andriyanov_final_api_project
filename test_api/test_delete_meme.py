import allure


# Позитивный тест: удаление существующего мема
@allure.feature("delete one meme")
@allure.story("Удаление одного мема")
def test_delete_meme_success(fixt_delete_meme, fixt_get_meme_id, fixt_get_one_meme):
    meme_id = fixt_get_meme_id  # id мема из фикстуры (создан заранее)
    fixt_delete_meme.full_req_delete_meme(meme_id)  # удаляем мем
    fixt_delete_meme.check_status_code(200)  # ожидаем статус 200
    # проверяем что мем действительно удалён
    fixt_get_one_meme.full_req_get_one_meme(meme_id)  # повторный GET должен вернуть 404
    fixt_get_one_meme.check_status_code(404)  # мем после удаления недоступен


# Негативный тест: повторное удаление уже удалённого мема
@allure.feature("delete one meme")
@allure.story("Ошибка при повторном удалении мема")
def test_delete_meme_already_deleted(fixt_delete_meme, fixt_get_meme_id):
    meme_id = fixt_get_meme_id  # id мема из фикстуры
    fixt_delete_meme.full_req_delete_meme(meme_id)  # первое удаление — успешно
    fixt_delete_meme.check_status_code(200)
    fixt_delete_meme.full_req_delete_meme(meme_id)  # повторное удаление — ошибка
    fixt_delete_meme.check_status_code(404)  # мем уже не существует


# Негативный тест: удаление несуществующего мема
@allure.feature("delete one meme")
@allure.story("Ошибка при удалении несуществующего мема")
def test_delete_meme_not_found(fixt_delete_meme):
    fixt_delete_meme.full_req_delete_meme(9999999)  # заведомо несуществующий id
    fixt_delete_meme.check_status_code(404)  # ожидаем ошибку 404


# Негативный тест: удаление мема без авторизации
@allure.feature("delete one meme")
@allure.story("Ошибка при удалении мема без токена")
def test_delete_meme_unauthorized(fixt_delete_meme, fixt_get_meme_id):
    meme_id = fixt_get_meme_id  # id мема из фикстуры
    fixt_delete_meme.full_req_delete_meme(
        meme_id, headers=fixt_delete_meme.BAD_TOKEN_HEADERS  # неверный токен
    )
    fixt_delete_meme.check_status_code(401)  # ожидаем ошибку 401
