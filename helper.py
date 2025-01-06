# This File have many functions that used in this program
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" 

def show_ship_data(ship):
    print(
            f"|{ship[0]:>11} | {ship[1]:<12} | {ship[2]:<14} | {ship[3]:<12} | {ship[4]:<10} | {ship[5]}   | {str(ship[6]):<10}     | "
            f"{ship[7]:<10} |"
        )
def show_docking_schedule_data(docking_schedule):
    print(
            f"|{docking_schedule[0]:>10}| {str(docking_schedule[1]):<20}| {docking_schedule[2]:<13}| {docking_schedule[3]:<14}|"
        )
    
def show_storage_zone_data(storage_zone):
    print(
        f"| {storage_zone[0]:>10} | {storage_zone[1]:<12} | {storage_zone[2]:<14} |"
    )

def show_container_data(container):
    print(
        f"| {container[0]:>8} | {container[1]:>12} | {container[2]:>16} | {container[3]:>9} |"
    )

def clear_console():
    print("\033[H\033[J")

def success_msg(text):
    clear_console()
    print(f"{GREEN}{text}{RESET}")

def danger_msg(text):
    clear_console()
    print(f"{RED}{text}{RESET}")

def warning_msg(text):
    clear_console()
    print(f"{YELLOW}{text}{RESET}")