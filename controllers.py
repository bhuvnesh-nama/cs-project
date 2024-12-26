from functions.ship import *
from functions.docking import *
from functions.storage_zone import *
from functions.container import *

from helper import clear_console,warning_msg

def ship_controller():
    while True:
        clear_console()
        print()
        print("--------------------------------------------------")
        print("-------           Ship Management          -------")
        print("--------------------------------------------------")

        print()
        print("1. Add new Ship")
        print("2. Get all Ships")
        print("3. Export all ships data into csv")
        print("4. Get Ships that arrives today")
        print("5. Export Ships that arrives today")
        print("6. Update ships")
        print("7. Delete ships")
        print()
        print("99. Exit")
        print()
        user = int(input("> "))

        if user == 1:
            add_new_ship()
        elif user == 2:
            get_all_ships()
        elif user == 3:
            path = input("Enter path >")
            export_all_ship_data_into_csv(path)
        elif user == 4:
            get_ships_arrives_today()
        elif user ==5:
            path = input("Enter path >")
            export_ships_arrives_today(path)
        elif user == 6:
            update_ship_by_id()
        elif user ==7:
            delete_ship_by_id()
        elif user == 99:
            break
        else:
            clear_console()
            warning_msg("Invalid Option!")

def docking_controller():
    while True:
        clear_console()
        print()
        print("--------------------------------------------------")
        print("-------        Docking Management          -------")
        print("--------------------------------------------------")
        print()
        print("1. Get Today Docking Schedules")
        print("2. Export Todays Docking Schedules")
        print("3. Get All Docking Schedules")
        print("4. Export All Docking Schedules")
        print("5. Add New Docking Schedule")
        print("6. Update Docking Schedule")
        print("7. Delete Docking Schedule")
        print()
        print("99. Exit")
        print()
        user = int(input(">"))

        if user ==1:
            get_todays_docking_schedules()
        elif user == 2:
            export_todays_docking_schedule()
        elif user == 3:
            get_all_docking_schedules()
        elif user == 4:
            export_all_docking_schedule()
        elif user == 5:
            add_new_docking_schedule()
        elif user == 6:
            update_docking_schedule()
        elif user == 7:
            delete_docking_schedule()
        elif user == 99:
            break
        else:
            warning_msg("Invalid option!")

def storage_zone_controller():
    while True:
        clear_console()
        print()
        print("--------------------------------------------------")
        print("-------       Storage Zone Mangement       -------")
        print("--------------------------------------------------")
        print()
        print("1. Add new storage zone")
        print("2. Get all storage zone")
        print("3. Update storage zone")
        print("4. Delete storage zone")
        print()
        print("99. Exit")
        print()

        user = int(input(">"))

        if user == 1:
            add_new_storage_zone()
        elif user ==2:
            get_all_storage_zone()
        elif user ==3:
            update_storage_zone()
        elif user ==4:
            delete_storage_zone()
        elif user ==99:
            break
        else:
            warning_msg("Invalid Option!")
            
def container_controller():
    while True:
        clear_console()
        print()
        print("--------------------------------------------------")
        print("-------       Container Management         -------")
        print("--------------------------------------------------")
        print()
        print("1. Add new container")
        print("2. Show all containers")
        print("3. update container")
        print("4. delete containers")
        print()
        print("99. Exit")
        print()

        user = int(input(">"))

        if user == 1:
            add_new_container()
        elif user == 2:
            show_all_containers()
        elif user == 3:
            update_container()
        elif user == 4:
            delete_container()
        elif user ==99:
            break
        else:
            warning_msg("Invalid Option!")
