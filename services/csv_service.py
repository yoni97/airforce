import csv


def save_at_csv(missions):
    missions_dict = [mission.to_dict() for mission in missions]
    print(missions_dict)
    with open('missions11.csv', 'w', newline='') as csvfile:
        fieldnames = ['Target City', 'Priority', 'Assigned Pilot' ,'Assigned Aircraft'
                 ,'Pilot Skill', 'Aircraft Speed', 'Aircraft Fuel Capacity']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(missions_dict)
        print("CSV file created successfully.")

