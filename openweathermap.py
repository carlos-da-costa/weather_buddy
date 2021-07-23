import requests
from requests import api


class Weather:

    _endpoints = {'current_city_weather': 'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'}

    def __init__(self, api_key) -> None:
        self._api_key = api_key

    def get_city_current_weather(self, city_name):
        params = {'city_name': city_name, 'api_key': self._api_key}
        response = requests.get(self._endpoints['current_city_weather'].format(**params))
        if response.status_code == 404:
            return None
        else:
            json = response.json()
            resp = {'weather': json['weather'][0]['description'],
                    'temperature': json['main']['temp']}
            return resp