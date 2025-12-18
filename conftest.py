import pytest
import copy

from endpoints.change_put_meme import ChangePutMeme
from endpoints.create_new_meme import CreateNewMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_one_meme import GetOneMeme
from endpoints.Authorization_token import GetAuthorizationToken
from endpoints.live_token import LiveToken


PAYLOAD = {
    "text": "memes if dog",
    "url": "https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg",
    "tags": ["dogs", "funny", "animals"],
    "info": {"author": "test_user", "rating": 5},
}  # базовый payload для создания мема

PAYLOAD_CHANGE = {
    "text": "memes if dogiies",
    "url": "https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg",
    "tags": ["doooogi", "super", "animals"],
    "info": {"author": "tester_user", "rating": 2},
}  # данные для последующего изменения мема


@pytest.fixture
def fixt_get_all_meme():
    return GetAllMeme()  # клиент для GET /meme


@pytest.fixture
def fix_create_new_meme():
    return CreateNewMeme()  # клиент для POST /meme


@pytest.fixture
def fixt_delete_meme():
    return DeleteMeme()  # клиент для DELETE /meme/{id}


@pytest.fixture
def fixt_get_meme_id(fix_create_new_meme, fixt_delete_meme):
    fix_create_new_meme.full_req_create_new_meme(payload=PAYLOAD)  # создаём мем для теста
    meme_id = fix_create_new_meme.meme_id  # сохраняем id созданного мема
    yield meme_id  # отдаём id в тест
    fixt_delete_meme.full_req_delete_meme(meme_id)  # чистим за собой после теста


@pytest.fixture
def fixt_payload_change():
    return copy.deepcopy(PAYLOAD_CHANGE)  # выдаём копию, чтобы тесты могли править поля


@pytest.fixture
def fixt_get_one_meme():
    return GetOneMeme()  # клиент для GET /meme/{id}


@pytest.fixture
def fixt_change_put_meme():
    return ChangePutMeme()  # клиент для PUT /meme/{id}


@pytest.fixture
def fixt_get_token():
    return GetAuthorizationToken()  # клиент для получения токена


@pytest.fixture
def fixt_is_alive_token():
    return LiveToken()  # клиент для проверки жив ли токен
