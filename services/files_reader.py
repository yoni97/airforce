import json
import math
from weather_conditions import *
import csv

#csv_targets_file = '../csv_files/air_strike_targets.csv'
aircrafts_json_file = '../json_files/aircrafts.json'
pilots_json_file = '../json_files/pilots.json'
targets_json_file = '../json_files/air_strike_targets.json'

def read_from_jason(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        return e

# print(read_from_jason(pilots_json_file))
list_of_pilots = sorted(read_from_jason(pilots_json_file), key=lambda k: k['skill_level'], reverse=True)
list_of_aircrafts = sorted(read_from_jason(aircrafts_json_file), key=lambda z: z['fuel_capacity'], reverse=True)
list_of_targets = sorted(read_from_jason(targets_json_file), key=lambda k: k['Priority'], reverse=True)
zip_to_missions = list(zip(list_of_pilots, list_of_aircrafts, list_of_targets))
print(zip_to_missions)



def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
    2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c
    return distance

get_geo = get_weather_geo('yaman')
LON2 = get_geo[0]['lon']
LAT2 = get_geo[0]['lat']
IL_LAT = 31.79592425
IL_LON = 35.211980759695

# print(haversine_distance(IL_LAT, IL_LON, LAT2, LON2))



weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.20,
    "pilot_skill" : 0.20,
    "weather_conditions" : 0.20,
    "execution_time" : 0.10,
"priority":0.15
}


def maped_cities():
    targets_dict = read_from_jason(targets_json_file)
    filtered_cities = list(map(lambda city: city['City'], [i for i in targets_dict]))
    return filtered_cities


def weather_score(weather):
    if weather['clouds'] == 'clear':
        return 1.0
    elif weather['clouds'] == 'clouds':
        return 0.7
    elif weather['clouds'] == 'rain':
        return 0.4
    elif weather['clouds'] == 'stormy':
        return 0.2
    else:
        return 0
