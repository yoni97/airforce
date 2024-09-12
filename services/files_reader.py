import json
import math
from weather_conditions import *

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

# print(read_from_jason(pilots_json_file))






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
    targets_dict = read_from_json(targets_json_file)
    filtered_cities = list(map(lambda city: city['City'], [i for i in targets_dict]))
    return filtered_cities







list_of_pilots = sorted(read_from_json(pilots_json_file), key=lambda k: k['skill_level'], reverse=True)
list_of_aircrafts = sorted(read_from_json(aircrafts_json_file), key=lambda z: z['fuel_capacity'], reverse=True)
list_of_targets = sorted(read_from_json(targets_json_file), key=lambda k: k['Priority'], reverse=True)
zip_to_missions = list(zip(list_of_pilots, list_of_aircrafts, list_of_targets))
print(zip_to_missions)