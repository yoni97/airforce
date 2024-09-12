from models import targets
from services.files_reader import read_from_json, pilots_json_file


class Pilots():
    def __init__(self, name: str, skill_level: int):
        self.name = name
        self.skill_level = skill_level



for pilot in read_from_json(pilots_json_file):
    pilot = Pilots(**pilot)
    print(pilot.name, pilot.skill_level)