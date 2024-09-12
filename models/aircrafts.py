from services.files_reader import read_from_json, aircrafts_json_file


class Aircraft():
    def __init__(self, type, speed, fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

for plain in read_from_json(aircrafts_json_file):
    plain = Aircraft(**plain)
    print(plain.type, plain.speed, plain.fuel_capacity)
