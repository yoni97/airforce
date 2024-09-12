import math

from services.files_reader import read_from_json, aircrafts_json_file, pilots_json_file
from services.weather_conditions import get_weather_geo
from services import *
from json_files import *



get_geo = get_weather_geo('yaman')
LON2 = get_geo[0]['lon']
LAT2 = get_geo[0]['lat']
IL_LAT = 31.79592425
IL_LON = 35.211980759695

def weather_score(self, __weather):
    return weather_score(__weather)

def get_weather(__target_city):
    return get_weather()

class Target():
    def __init__(self, city: str, lat: float, lon: float, priority: int):
        self.__city = city
        self.__lat = lat
        self.__lon = lon
        self.__priority = priority
        self.__weather = get_weather(self.__target_city)
        self.__distance = self.haversine_distance()
        self.__weather_score = self.weather_score(self.__weather)

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
        return distance

    # @staticmethod
    # def weather_score(self, weather):
    #     if weather['clouds'] == 'clear':
    #         return 1.0
    #     elif weather['clouds'] == 'clouds':
    #         return 0.7
    #     elif weather['clouds'] == 'rain':
    #         return 0.4
    #     elif weather['clouds'] == 'stormy':
    #         return 0.2
    #     else:
    #         return 0

    def lat(self):
        return LAT2

    def lon(self):
        return LON2
for plain in read_from_json(aircrafts_json_file):
    for pilot in read_from_json(pilots_json_file):
        for target in read_from_json(aircrafts_json_file):

def generate_missions(target_cities, aircrafts, pilots):
    missions = []
    for key, city in target_cities.items():
        for key, aircraft in aircrafts.items():
            for key, pilot in pilots.items():
                missions.append(Attack(
                    city.city,
                    city.priority,
                    pilot.name,
                    aircraft.type,
                    city.distance,
                    city.weather_score,
                    city.weather_conditions,
                    pilot.skill_level,
                    aircraft.speed,
                    aircraft.fuel_capacity))
    return missions