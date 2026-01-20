
PAYLOAD = {
    "text": "memes if dog",
    "url": "https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg",
    "tags": ["dogs", "funny", "animals"],
    "info": {"author": "test_user", "rating": 5},
}

# Невалидные варианты — по одному полю None
BADBODY_NO_TEXT = {**PAYLOAD, "text": None}
BADBODY_NO_URL = {**PAYLOAD, "url": None}
BADBODY_NO_TAGS = {**PAYLOAD, "tags": None}
BADBODY_NO_INFO = {**PAYLOAD, "info": None}

BADDATA = [BADBODY_NO_TEXT, BADBODY_NO_URL, BADBODY_NO_TAGS, BADBODY_NO_INFO]

# Позитивные варианты — пустые значения правильного типа
PAYLOAD_EMPTY_TEXT = {**PAYLOAD, "text": ""}
PAYLOAD_EMPTY_URL = {**PAYLOAD, "url": ""}
PAYLOAD_EMPTY_TAGS = {**PAYLOAD, "tags": []}
PAYLOAD_EMPTY_INFO = {**PAYLOAD, "info": {}}

GOODDATA = [PAYLOAD, PAYLOAD_EMPTY_TEXT, PAYLOAD_EMPTY_URL, PAYLOAD_EMPTY_TAGS, PAYLOAD_EMPTY_INFO]

PAYLOAD_CHANGE = {
    "text": "memes if dogiies",
    "url": "https://memi.klev.club/uploads/posts/2024-04/memi-klev-club-19lu-p-memi-s-dovolnoi-sobakoi-31.jpg",
    "tags": ["doooogi", "super", "animals"],
    "info": {"author": "tester_user", "rating": 2},
}  # данные для последующего изменения мема