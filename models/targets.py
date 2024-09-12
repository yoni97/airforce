import math
from services import *
from json_files import *
from services.weather_conditions import get_weather_geo

aircrafts_json_file = '../json_files/aircrafts.json'
pilots_json_file = '../json_files/pilots.json'
targets_json_file = '../json_files/air_strike_targets.json'


def read_weather(__target_city):
    pass


class Target():
    def __init__(self, target_city: str, lat: float, lon: float, priority: int):
        self.__target_city = target_city
        self.__lat = lat
        self.__lon = lon
        self.__priority = priority
        self.__weather = read_weather(self.__target_city)
        self.__distance = self.haversine_distance()
        self.__weather_score = self.weather_score(self.__weather)

    def haversine_distance(lat1, lon1, lat2, lon2):
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

    get_geo = get_weather_geo('yaman')
    LON2 = get_geo[0]['lon']
    LAT2 = get_geo[0]['lat']
    IL_LAT = 31.79592425
    IL_LON = 35.211980759695

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