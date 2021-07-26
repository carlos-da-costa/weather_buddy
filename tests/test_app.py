import unittest
from unittest import mock
import json

from app import app as flask_app

class TestApp(unittest.TestCase):

    client = flask_app.test_client()
    
    @mock.patch('openweathermap.requests.get')
    def test_city_by_name(self, mock_get):
        mock_response = mock.Mock(status_code=200) 
        with open('tests/get_city_current_weather.json') as json_file:
            resp_json = json.loads(json_file.read())
        mock_response.json.return_value = resp_json
        mock_response.return_value.ok = True
        mock_get.return_value = mock_response

        response = self.client.get('/weather/london')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['temperature'], 16.81)

    @mock.patch('openweathermap.requests.get')
    def test_city_by_name_not_found(self, mock_get):
        mock_response = mock.Mock(status_code=404) 
        with open('tests/city_not_found.json') as json_file:
            resp_json = json.loads(json_file.read())
        mock_response.json.return_value = resp_json
        mock_response.return_value.ok = True
        mock_get.return_value = mock_response

        response = self.client.get('/weather/londox')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('city not found' in str(response.get_data()))