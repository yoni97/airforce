from services import algorithms
from services.algorithms import list_of_pilots, list_of_aircrafts, list_of_targets
from services.csv_service import save_at_csv



class Execute_missions():

    def __init__(self, city, priority, name , skill_level, speed, fuel_capacity, type):
        self.city = city
        self.priority = priority
        self.name = name
        self.skill_level = skill_level
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.type = type



    def get_string(self):
        return (
            f"Target City: {self.city}\n"
            f"Priority: {self.priority}\n"
            f"Assigned Pilot: {self.name}\n"
            f"Assigned Aircraft: {self.type}\n"
            f"Pilot Skill: {self.skill_level}\n"
            f"Aircraft Speed: {self.speed} km/h\n"
            f"Aircraft Fuel Capacity: {self.fuel_capacity} liters\n"
            f"\n"
        )

        def get_mission_fit_score(self):
            score = algorithms.get_distance_score(self.distance)
            score += algorithms.get_priority_score(self.priority)
            score += algorithms.get_pilot_skill_score(self.pilot_skill)
            score += algorithms.get_aircraft_fuel_score(self.aircraft_fuel_Capacity)
            score += algorithms.get_weather_conditions_score(self.weather_conditions)
            score += algorithms.get_execution_time_score()
            self.mission_fit_score = score
        return get_mission_fit_score

    def to_dict(self):
        new_dict =  {
            "Target City": self.city,
            "Priority": self.priority,
            "Assigned Pilot": self.name,
            "Assigned Aircraft": self.type,
            "Pilot Skill": self.skill_level,
            "Aircraft Speed": self.speed,
            "Aircraft Fuel Capacity": self.fuel_capacity,
        }
        return new_dict


def create_mission(list_of_pilots, list_of_aircrafts, list_of_targets):
    missions = []
    for city in list_of_targets:
        for aircraft in list_of_aircrafts:
            for pilot in list_of_pilots:
                missions.append(Execute_missions(
                    city['City'],
                    city["Priority"],
                    pilot['name'],
                    pilot['skill_level'],
                    aircraft['speed'],
                    aircraft['fuel_capacity'],
                    aircraft['type'],
                ))
    return missions


save_at_csv(create_mission(list_of_pilots, list_of_aircrafts, list_of_targets))











