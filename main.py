from db.connect import Database
from settings import MigrationManager
import sys
import pyfiglet


# Importing Controllers
from controllers import *
def main():
    Database.get_connection()

    args = sys.argv
    if not len(args) == 1:
        if args[1] == "makemigration":
            is_migrated = MigrationManager.run()
            if is_migrated:
                print("Migration successfully!")
                exit()
    
    # print("--------------------------------------------------")
    # print("-------           Ship Management          -------")
    # print("--------------------------------------------------")
    

    print(pyfiglet.figlet_format("Welcome To Port Management",font="small"))

    while True:
        print("1. Ship Management")
        print("2. Docking Management")
        print("3. Storage Zone Management")
        print("4. Container Management")
        print()
        print("99. Exit")
        print()

        user = int(input(">"))
        
        if user == 1:
            clear_console()
            print()
            print("--------------------------------------------------")
            print("-------           Ship Management          -------")
            print("--------------------------------------------------")

            ship_controller()
        elif user == 2:
            clear_console()
            print()
            print("--------------------------------------------------")
            print("-------        Docking Management          -------")
            print("--------------------------------------------------")
            
            docking_controller()
        elif user ==3:
            clear_console()
            print()
            print("--------------------------------------------------")
            print("-------       Storage Zone Mangement       -------")
            print("--------------------------------------------------")
            
            storage_zone_controller()
        elif user ==4:
            clear_console()
            print()
            print("--------------------------------------------------")
            print("-------       Container Management         -------")
            print("--------------------------------------------------")
            
            container_controller()
        elif user == 99:
            break
        else:
            warning_msg("Invalid Operation!")
    

if __name__ == "__main__":
    main()