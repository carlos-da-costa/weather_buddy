from os import lseek
from flask import Flask
from flask import abort
from flask import request
from flask import jsonify
from flask_caching import Cache
import openweathermap

app = Flask(__name__)
app.config.from_pyfile('config.py')
cache = Cache(app)

CACHE_SIZE = app.config["CACHE_SIZE"]
API_KEY = app.config['API_KEY']

@app.route('/weather')
def weather_in_cache(methods=['GET']):
    max_number = request.args.get('max_number', type=int, default=CACHE_SIZE)
    
    last_cities = cache.get("last_cities") or {}
    
    result = {}
    if max_number < CACHE_SIZE:
        for key in list(last_cities.keys())[:max_number]:
            result[key] = last_cities[key]
    else:
        result = last_cities
    
    return jsonify(result)
    

@app.route('/weather/<city_name>')
def weather_by_city(city_name, methods=['GET']):
    weather = openweathermap.Weather(API_KEY)
    
    last_cities = cache.get("last_cities") or {}

    if city_name in last_cities.keys():
        return jsonify(last_cities[city_name])
    else:
        resp = weather.get_city_current_weather(city_name)
        if resp:
            len_cache = len(last_cities.keys())
            if len_cache < CACHE_SIZE:
                last_cities[city_name] = resp
            else:
                oldest_key = list(last_cities.keys())[0]
                del last_cities[oldest_key]
                last_cities[city_name] = resp
                
            cache.set("last_cities", last_cities)

            return jsonify(resp)
        else:
            abort(404, 'city not found')

        
        