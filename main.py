from db.connect import Database
from settings import MigrationManager
import sys



# Importing Controllers
from controllers import *
def main():
    Database.get_connection()

    args = sys.argv
    if not len(args) == 1:
        if args[1] == "makemigration":
            MigrationManager.run()
    
    print("--------------------------------------------------")
    print("-------     Welcome To Port Management     -------")
    print("--------------------------------------------------")
    while True:
        print("1. Ship Management")
        print("99. Exit")
        print()

        user = int(input(">"))
        
        if user == 1:
            ship_controller()
        if user == 99:
            break
    

if __name__ == "__main__":
    main()