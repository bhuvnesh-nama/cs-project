from db.models import Ship
import csv
from datetime import datetime
import uuid

random_value = uuid.uuid4()
todays_date = datetime.now().strftime("%Y-%m-%d")

def show_data(ship):
    print(
            f"{ship[0]:>11} | {ship[1]:<12} | {ship[2]:<12} | {ship[3]:<14} | "
            f"{ship[4]:<12} | {ship[5]:<10} | {ship[6]}   | {ship[7]}     | "
            f"{ship[8]:<10} |"
        )
def add_new_ship():
    ship = Ship(name="Titanic", type="Cargo", weight=1.5, flag="India", capacity=8, arrival_date="2608-09-07",departure_date="2820-09-07", status="Upcomming")
    ship.save()

def get_all_ships():
    data = Ship.get()
    print("     id     |     name     |     type     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 134)

    for ship in data:
        show_data(ship)

def export_all_ship_data_into_csv(path):
    data = Ship.get()
    with open(f"{path}\\{random_value}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name","type","weight","flag","capacity", "arrival_date","departure_date", "status"])
        writer.writerows(data)
        
def get_ships_arrives_today():
    data = Ship.get(arrival_date=todays_date)
    print("     id     |     name     |     type     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 134)

    for ship in data:
        show_data(ship)

def export_ships_arrives_today(path):
    data = Ship.get(arrival_date=todays_date)
    with open(f"{path}\\{random_value}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name","type","weight","flag","capacity", "arrival_date","departure_date", "status"])
        writer.writerows(data)

def update_ship_by_id():
    id = int(input("Enter Ship id >"))
    print("What you want to update ?")
    print("1. Name")
    print("2. type")
    print("3. weight")
    print("4. capacity")
    print("5. flag")
    print("6. arrival_date (yyyy-mm-dd)")
    print("7. departure_date (yyyy-mm-dd)")

    option = int(input(">"))

    if option ==1:
        "0"
