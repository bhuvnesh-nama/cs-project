# Functions For Docking Management
from db.models import DockingSchedule,Ship
from datetime import datetime
from helper import *
from uuid import uuid4
import csv

random_value = uuid4()
todays_date = datetime.now().strftime("%Y-%m-%d")

# To Add New Docking Schedule
def add_new_docking_schedule():
    clear_console()
    ships = Ship.get()
    print("-" * 119)
    print("|     id     |     name     |     weight     |     flag     |  capacity  | arrival_date | departure_date |   status   |")
    print("-" * 119)
    for ship in ships:
        show_ship_data(ship)
    print("-" * 119)
    print()
    ship_id = int(input("Enter ship id :"))
    
    schedule_date = input("Enter Schedule Date (YYYY-MM-DD) or t for todays date :")
    if schedule_date == "t":
        schedule_date = todays_date
    dock_schedule = DockingSchedule(schedule_date=schedule_date, ship_id=ship_id, status="Upcomming")
    dock_schedule.save()

    success_msg("Docking Schedule addedd successfully!")

# To Get All Docking Schedule
def get_all_docking_schedules():
    docking_schedules = DockingSchedule.get()
    print("-"*65)
    print("|    id    |    Schedule Date    |    Status    |    ship_id    |")
    print("-"*65)
    for dock_schedule in docking_schedules:
        show_docking_schedule_data(dock_schedule)
    print("-"*65)
    input("Enter to quit:")

# To Get Todays Docking Schedule
def get_todays_docking_schedules():
    docking_schedules = DockingSchedule.get(schedule_date=todays_date)
    if docking_schedules == ():
        warning_msg("No Docking Schedules!")
    else:
        print("-"*65)
        print("|    id    |    Schedule Date    |    Status    |    ship_id    |")
        print("-"*65)
        for dock_schedule in docking_schedules:
            show_docking_schedule_data(dock_schedule)
        print("-"*65)
    input("Enter to quit:")

# To Export Todays Docking Schedule Into CSV File
def export_todays_docking_schedule():
    docking_schedules = DockingSchedule.get(schedule_date=todays_date)
    path = input("Enter path >")
    with open(f"{path}/{random_value}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "Schedule Date", "Status", "ship_id"])
        writer.writerows(docking_schedules)

    success_msg("CSV exported successfully!")

# To Export All docking Schedule Into CSV File
def export_all_docking_schedule():
    docking_schedules = DockingSchedule.get()
    path = input("Enter path >")
    with open(f"{path}/{random_value}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "Schedule Date", "Status", "ship_id"])
        writer.writerows(docking_schedules)

    success_msg("CSV exported successfully!")

# To Update Docking Schedule
def update_docking_schedule():
    docking_schedules = DockingSchedule.get()
    print("-"*65)
    print("|    id    |    Schedule Date    |    Status    |    ship_id    |")
    print("-"*65)
    for dock_schedule in docking_schedules:
        show_docking_schedule_data(dock_schedule)
    print("-"*65)

    id = int(input("Enter id >"))

    print("What you want to update?")
    print("1. Schedule Date")
    print("2. Status")
    print()
    option = int(input(":"))
    if option == 1:
        schedule_date= input("Enter date (YYYY-MM-DD) or press t for todays date")
        DockingSchedule.update_by_id(id=id, schedule_date=schedule_date)
        success_msg("Docking Schedule Updated Successfully!")
    elif option==2:
        status = int(input("Status\n1. Pending\n2. Docking\n3. Docked\n:"))
        if status == 1:
            status == "Pending"
        elif status == 2:
            status == "Docking"
        elif status == 3:
            status == "Docked"
        DockingSchedule.update_by_id(id=id, status=status)

        success_msg("Docking Schedule Updated Successfully!")
    else:
        warning_msg("Invalid Option!")

# To Delete Docking Schedule
def delete_docking_schedule():
    docking_schedules = DockingSchedule.get()
    print("-"*65)
    print("|    id    |    Schedule Date    |    Status    |    ship_id    |")
    print("-"*65)
    for dock_schedule in docking_schedules:
        show_docking_schedule_data(dock_schedule)
    print("-"*65)

    id = int(input("Enter id :"))
    danger_msg("Are you sure you want to delete docking schedule with id {id} (y/n) :")
    opt = input()
    if opt == 'y' or opt =='Y':
        DockingSchedule.delete_by_id(id=id)
        success_msg("Docking Schedule deleted successfully!")
    else:
        warning_msg("Cancelled by user")
    