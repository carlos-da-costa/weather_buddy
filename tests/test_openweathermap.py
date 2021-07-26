import unittest
from unittest import mock
import json

from openweathermap import Weather

class TestApi(unittest.TestCase):

    @mock.patch('openweathermap.requests.get')
    def test_weather_by_city(self, mock_get):
        mock_response = mock.Mock(status_code=200) 
        with open('tests/get_city_current_weather.json') as json_file:
            resp_json = json.loads(json_file.read())
        mock_response.json.return_value = resp_json
        mock_response.return_value.ok = True
        mock_get.return_value = mock_response

        weather = Weather('1234567890')
        response = weather.get_city_current_weather('london')
        self.assertEqual(response['city_name'], 'london')
        self.assertEqual(response['weather'], 'broken clouds')
        self.assertEqual(response['temperature'], 16.81)
    
    @mock.patch('openweathermap.requests.get')
    def test_weather_by_city(self, mock_get):
        mock_response = mock.Mock(status_code=404) 
        with open('tests/city_not_found.json') as json_file:
            resp_json = json.loads(json_file.read())
        mock_response.json.return_value = resp_json
        mock_response.return_value.ok = True
        mock_get.return_value = mock_response

        weather = Weather('1234567890')
        response = weather.get_city_current_weather('random city name')
        self.assertEqual(response, None)