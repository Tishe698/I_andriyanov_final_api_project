import pytest

from endpoints.change_put_meme import ChangePutMeme
from endpoints.create_new_meme import CreateNewMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_one_meme import GetOneMeme


PAYLOAD = {
    'text': 'memes if dog',
    'url': 'https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg',
    'tags': ['dogs', 'funny', 'animals'],
    'info': {'author': 'test_user', 'rating': 5}
}

PAYLOAD_CHANGE = {
    'text': 'memes if dogiies',
    'url': 'https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg',
    'tags': ['dogs', 'funny', 'animals'],
    'info': {'author': 'test_user', 'rating': 5}
}



@pytest.fixture
def fixt_get_all_meme():
    return GetAllMeme()

@pytest.fixture
def fix_create_new_meme():
    return CreateNewMeme()

@pytest.fixture
def fixt_delete_meme():
    return DeleteMeme()


@pytest.fixture
def fixt_get_post_id(fix_create_new_meme, fixt_delete_meme):
    fix_create_new_meme.full_req_create_new_meme(payload=PAYLOAD)
    post_id = fix_create_new_meme.post_id
    yield post_id
    fixt_delete_meme.full_req_delete_meme(post_id)

@pytest.fixture
def fixt_get_one_meme():
    return GetOneMeme()

@pytest.fixture
def fixt_change_put_meme():
    return ChangePutMeme()

