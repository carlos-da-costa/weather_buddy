from os import lseek
from flask import Flask
from flask import abort
from flask import jsonify
from flask_caching import Cache
import requests
import openweathermap


API_key = '20b34da68d9d55e4b528dd0726aed83c'

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "FileSystemCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 3000,
    "CACHE_DIR": 'cache'
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
cache_size = 5

@app.route('/weather/<city_name>')
def profile(city_name):
    weather = openweathermap.Weather(API_key)
    
    last_cities = cache.get("last_cities") or {}
    print(last_cities)

    if city_name in last_cities.keys():
        return jsonify(last_cities[city_name])
    else:
        resp = weather.get_city_current_weather(city_name)
        if resp:
            len_cache = len(last_cities.keys())
            if len_cache < cache_size:
                last_cities[city_name] = resp
            else:
                oldest_key = list(last_cities.keys())[0]
                del last_cities[oldest_key]
                last_cities[city_name] = resp
                
            cache.set("last_cities", last_cities)

            return jsonify(resp)
        else:
            abort(404, 'city not found')

        
        