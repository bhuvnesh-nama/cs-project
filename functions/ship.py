from db.models import Ship
import csv
from datetime import datetime
import uuid

from helper import show_ship_data,success_msg,danger_msg,warning_msg,clear_console


random_value = uuid.uuid4()
todays_date = datetime.now().strftime("%Y-%m-%d")


    

def add_new_ship():
    name = input("Name :")
    weight = float(input("Weight (in tons) :"))
    capacity = float(input("Capacity (in containers):"))
    flag = input("Flag :")
    arrival_date = input("Arrival Date (YYYY-MM-DD)/ press t for today date :")
    status = "In Transit"
    if arrival_date == "t":
        arrival_date = todays_date
    
    ship = Ship(name=name, weight=weight, flag=flag, capacity=capacity, arrival_date=arrival_date, status=status)
    ship.save()

    success_msg("Ship Addedd Successfully!")
def get_all_ships():
    clear_console()
    data = Ship.get()
    print("-" * 119)
    print("|     id     |     name     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 119)

    for ship in data:
        show_ship_data(ship)
    print("-" * 119)
    input("enter to quit:")

def export_all_ship_data_into_csv(path):
    data = Ship.get()
    with open(f"{path}\\{random_value}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name","weight","flag","capacity", "arrival_date","departure_date", "status"])
        writer.writerows(data)
    
    success_msg("Data exported successfully!")
        
def get_ships_arrives_today():
    clear_console()
    data = Ship.get(arrival_date=todays_date)
    print("-" * 119)
    print("|     id     |     name     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 119)

    for ship in data:
        show_ship_data(ship)
    print("-" * 119)
    input("enter to quit:")

def export_ships_arrives_today(path):
    data = Ship.get(arrival_date=todays_date)
    with open(f"{path}\\{random_value}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name","weight","flag","capacity", "arrival_date","departure_date", "status"])
        writer.writerows(data)

    success_msg("Exported Successfully")

def update_ship_by_id():
    data = Ship.get()
    print("-" * 119)
    print("|     id     |     name     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 119)

    for ship in data:
        show_ship_data(ship)
    print("-" * 119)

    id = int(input("Enter Ship id >"))
    print("What you want to update ?")
    print("1. Name")
    print("2. weight")
    print("3. capacity")
    print("4. flag")
    print("5. arrival_date (yyyy-mm-dd)")
    print("6. departure_date (yyyy-mm-dd)")
    print("7. Status")

    option = int(input(">"))

    if option ==1:
        name = input("Enter name :")
        Ship.update_by_id(id, name=name)
    elif option ==2:
        weight = float(input("Weight (in tons) :"))
        Ship.update_by_id(id, weight=weight)
    elif option ==3:
        capacity = int(input("Capacity (in containers):"))
        Ship.update_by_id(id, capacity=capacity)
    elif option ==4:
        flag = input("Flag :")
        Ship.update_by_id(id, flag=flag)
    elif option ==5:
        arrival_date = input("Arrival Date (YYYY-MM-DD)/ press t for today date :")
        if arrival_date=="t":
            arrival_date= todays_date
        Ship.update_by_id(id, arrival_date=arrival_date)
    elif option ==6:
        departure_date = input("Departure Date (YYYY-MM-DD) :")
        Ship.update_by_id(id, departure_date=departure_date)
    elif option == 7:
        status = int(input("Status\n1. In Transit\n2. Arrived\n3. In Dock\n4. Docked\n5. Departed\n:"))
        if status == 1:
            status = "In Transit"
        elif status ==2:
            status = "Arrived"
        elif status ==3:
            status = "In Dock"
        elif status ==4:
            status = "Docked"
        elif status ==5:
            status = "Departed"
        else:
            warning_msg("Invalid Option!")
        
        Ship.update_by_id(id, status=status)
    success_msg(f"Ship with id {id} updated successfully!")


def delete_ship_by_id():
    ship = Ship.get()
    if not ship:
        warning_msg("No ship found")
        return
    print("-" * 119)
    print("|     id     |     name     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 119)
    show_ship_data(ship[0])
    print("-" * 119)

    id = int(input("Enter id >"))
    user = input("Do you want to delete this ship (y/n) :")

    if user == 'y' or user == 'Y':
        ship_exists = Ship.get(id=id)
        if ship_exists:
            Ship.delete_by_id(id)
            success_msg("Ship deletd successfully")
        else:
            warning_msg("Ship does not exists")
    elif user == 'n' or user == 'N':
        warning_msg("Cancelled by user!")
    else:
        warning_msg("Invalid Option!")
