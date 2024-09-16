import math
from services.algorithms import calculate_weather
from services.files_reader import read_from_json, aircrafts_json_file, pilots_json_file
from services.weather_conditions import get_weather_geo
from services import *
from json_files import *



get_geo = get_weather_geo('yemen')
LON2 = get_geo[0]['lon']
LAT2 = get_geo[0]['lat']
IL_LAT = 31.79592425
IL_LON = 35.211980759695

class Target():
    def __init__(self, city: str, priority: int, distance, total_weather_score):
        self.city = city
        self.priority = priority
        self.distance = distance
        self.total_weather_score = total_weather_score

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        r = 6371.0
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
                                                                                         2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = r * c
        self.distance = distance
        return self.distance



