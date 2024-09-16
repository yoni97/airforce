import json
import math
# from weather_conditions import *

aircrafts_json_file = '../json_files/aircrafts.json'
pilots_json_file = '../json_files/pilots.json'
targets_json_file = '../json_files/air_strike_targets.json'

def read_from_json(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        return e

# print(json.dumps(read_from_json(aircrafts_json_file), indent=4, ensure_ascii=False))

weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.20,
    "pilot_skill" : 0.20,
    "weather_conditions" : 0.20,
    "priority":0.25
}


def maped_cities():
    targets_dict = read_from_json(targets_json_file)
    filtered_cities = list(map(lambda city: city['City'], [i for i in targets_dict]))
    return filtered_cities












