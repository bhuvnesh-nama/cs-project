from functions.ship import *

def ship_controller():
    while True:
        print("1. Add new Ship")
        print("2. Get all Ships")
        print("3. Export all ships data into csv")
        print("4. Get Ships that arrives today")
        print("5. Export Ships that arrives today")
        print("6. Update ships by id")
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
        if user == 99:
            break