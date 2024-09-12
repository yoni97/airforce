from services.weather_conditions import *


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

def get_weather():
    weather = get_weather_temperature(city)
    temp = weather["list"][0]["clouds"]["all"]
    return temp
# print(get_weather(city))

def get_wind():
    weather = get_weather_temperature(city)
    wind = weather["list"][0]["wind"]["speed"]
    return wind

def str_weather():
    weather = get_weather_temperature(city)
    string_weather = weather["list"][0]["weather"][0]["main"]
    return string_weather

def weather_score(weather):
    if weather['clouds'] == 'clear':
        return 100
    elif weather['clouds'] == 'clouds':
        return 70
    elif weather['clouds'] == 'rain':
        return 40
    elif weather['clouds'] == 'stormy':
        return 20
    else:
        return 0

number_of_the_weather = get_weather()
wind = get_wind()
score = weather_score(str_weather())

def calculate_weather(number_of_the_weather, wind, score):
    return number_of_the_weather + score * wind





