import math
import random
from services.files_reader import read_from_json, targets_json_file, pilots_json_file, aircrafts_json_file
from services.weather_conditions import *

def maped_cities():
    targets_dict = read_from_json(targets_json_file)
    filtered_cities = list(map(lambda city: city['City'], [i for i in targets_dict]))
    return filtered_cities


def filter_the_weather_all_countries():
    list_of_cities_weathers = []
    for city in maped_cities():
        get_weather = get_weather_temperature(city)
        new_dict = {}

        new_dict["lat"] = get_weather["city"]["coord"]["lat"]
        new_dict["lon"] = get_weather["city"]["coord"]["lon"]
        new_dict["weather"] = get_weather["list"][0]["weather"][0]["main"]
        new_dict["clouds"] = get_weather["list"][0]["clouds"]["all"]
        new_dict["wind"] = get_weather["list"][0]["wind"]["speed"]
        new_dict["dt_txt"] = get_weather["list"][2]["dt_txt"]
        list_of_cities_weathers.append(new_dict)
    return list_of_cities_weathers
# print(json.dumps(filter_the_weather(), indent=4, sort_keys=True))



def filter_the_weather():
    get_weather = get_weather_temperature(city)
    new_dict = {}

    new_dict["lat"] = get_weather["city"]["coord"]["lat"]
    new_dict["lon"] = get_weather["city"]["coord"]["lon"]
    new_dict["weather"] = get_weather["list"][0]["weather"][0]["main"]
    new_dict["clouds"] = get_weather["list"][0]["clouds"]["all"]
    new_dict["wind"] = get_weather["list"][0]["wind"]["speed"]
    new_dict["dt_txt"] = get_weather["list"][2]["dt_txt"]
    return new_dict
# print(filter_the_weather())

def get_weather():
    weather = filter_the_weather()
    temp = weather["clouds"]
    return temp

def get_wind():
    weather = filter_the_weather()
    wind = weather["wind"]
    return wind
# print(get_wind())

def dictionary_weather():
    my_dict = {}
    weather = get_weather_temperature(city)
    my_dict['clouds'] = weather["list"][0]["weather"][0]["main"]
    return my_dict

def weather_score(weather):
    if weather['clouds'] == 'Clear':
        return 1.0
    elif weather['clouds'] == 'Clouds':
        return 0.7
    elif weather['clouds'] == 'rain':
        return 0.4
    elif weather['clouds'] == 'Stormy':
        return 0.2
    else:
        return 0
# print(weather_score(dictionary_weather()))

number_of_the_weather = get_weather()
wind = get_wind()
score = weather_score(dictionary_weather())
# print(f'number_of_the_weather {number_of_the_weather}, wind {wind}, score {score}')

def calculate_weather(number_of_the_weather, wind, score):
    return number_of_the_weather + score * wind
# print(calculate_weather(number_of_the_weather, wind, score))

def get_distance_score(distance):
    magic_number = (100/distance)* 150
    if magic_number > 150:
        return 150
    if magic_number < 1:
        return 1
    return magic_number

def get_aircraft_fuel_score(aircraft_fuel_Capacity):
    magic_number = (4000/aircraft_fuel_Capacity)*200
    if magic_number > 200:
        return 200
    if magic_number < 1:
        return 1
    return magic_number


def get_execution_time_score():
    return random.uniform(1, 100)


def get_pilot_skill_score(pilot_skill):
    return pilot_skill * 20


def get_weather_conditions_score(weather_conditions: int):
    return int(weather_conditions) * 200


def get_priority_score(priority: int):
    return priority * 150/6


list_of_pilots = sorted(read_from_json(pilots_json_file), key=lambda k: k['skill_level'], reverse=True)
list_of_aircrafts = sorted(read_from_json(aircrafts_json_file), key=lambda z: z['fuel_capacity'], reverse=True)
list_of_targets = sorted(read_from_json(targets_json_file), key=lambda k: k['Priority'], reverse=True)
