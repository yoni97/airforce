import requests
import json
# from files_reader import *



my_key = ''
city = 'yemen'
my_loc = ''

# def maped_cities():
#     targets_dict = read_from_json(targets_json_file)
#     filtered_cities = list(map(lambda city: city['City'], [i for i in targets_dict]))
#     return filtered_cities

def get_weather_temperature(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=55d034e4413bb6e5ecc16af4a6300c1c"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"
# print(get_weather_temperature(city, my_key))

def get_weather_geo(city):
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=55d034e4413bb6e5ecc16af4a6300c1c'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"
# print(get_weather_geo(city, my_key))

def geo_coordinates(city):
    get_geo = get_weather_geo(city)

    new_dict = {}
    new_dict['lon'] = get_geo[0]['lon']
    new_dict['lat'] = get_geo[0]['lat']
    return new_dict
# print(geo_coordinates(city))


def filter_the_weather():
    get_weather = get_weather_temperature(city)
    new_dict = {}

    new_dict["lat"] = get_weather["city"]["coord"]["lat"]
    new_dict["lon"] = get_weather["city"]["coord"]["lon"]
    new_dict["weather"] = get_weather["list"][0]["weather"][0]["main"]
    new_dict["clouds"] = get_weather["list"][0]["clouds"]["all"]
    new_dict["wind"] = get_weather["list"][0]["wind"]["speed"]
    new_dict["dt_txt"] = get_weather["list"][3]["dt_txt"]
    return new_dict
# print(filter_the_weather())

def get_weather(city):
    weather = get_weather_temperature(city)
    w = weather["list"][0]["clouds"]["all"]
    return w
# print(get_weather(city))

def get_wind():
    weather = get_weather_geo(city)
    wind = weather["list"][0]["wind"]["speed"]

number_of_theweather = get_weather(city)

# def calculate_weather(get_weather, ):




