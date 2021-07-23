from flask import Flask
from flask import abort
from flask import jsonify
import requests


API_key = '20b34da68d9d55e4b528dd0726aed83c'

app = Flask(__name__)

@app.route('/weather/<city_name>')
def profile(city_name):
    endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
    response = requests.get(endpoint)
    if response.status_code == 404:
        abort(404, 'city not found')
    elif response.status_code == 200:
        json = response.json()
        resp = {'weather': json['weather'][0]['description'],
                'temperature': json['main']['temp']}
        return jsonify(resp)
