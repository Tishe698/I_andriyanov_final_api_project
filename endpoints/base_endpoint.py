import requests
import allure

class BaseEndpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    _token = None

    def __init__(self):
        # Если токена нет или токен невалидный получаем токен
        if not self._token or not self.is_token_valid():
            self._token = self.get_new_token()
        self.headers = {'content-type': 'application/json',
                        'authorization': self._token}


    def is_token_valid(self):
        response = requests.get(
            url = f'{self.url}/authorize/{self._token}')
        return response.status_code == 200


    def get_new_token(self):
        response = requests.post(
            url = f'{self.url}/authorize',
            json = {
                'name' : 'ivan_andriyanov'
            },
            headers = {'content-type' : 'application/json'},
        )
        token = response.json()['token']
        return token

    @allure.step('Check that response is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200




