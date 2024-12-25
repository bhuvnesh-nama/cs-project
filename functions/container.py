from db.models import StorageZone, Container, Ship

from helper import *

def add_new_container():
    weight = float(input("Weight (in tons) :"))
    storage_zone_id = int(input("Storage zone id :"))
    ship_id = int(input("Ship id :"))

    storage_zone_exists= StorageZone.get(id=storage_zone_id)
    if not storage_zone_exists:
        warning_msg("Storage zone not exists")
        return
    ship_exists = Ship.get(id=ship_id)

    if not ship_exists:
        warning_msg("Ship not exists")

    if ship_exists and storage_zone_exists:
        container = Container(weight=weight,storage_zone_id=storage_zone_id, ship_id=ship_id)
        container.save()


def show_all_containers():
    clear_console()
    containers = Container.get()
    print("-"*58)
    print("|    id    |    weight    |  storage_zone_id |  ship_id  |")
    print("-"*58)
    for container in containers:
        show_container_data(container)
    print("-"*58)
    
def update_container():
    clear_console()
    containers = Container.get()
    print("-"*58)
    print("|    id    |    weight    |  storage_zone_id |  ship_id  |")
    print("-"*58)
    for container in containers:
        show_container_data(container)
    print("-"*58)
    id = int(input("Enter id :"))
    print("What you want to update?")
    print("1. Weight")
    print("2. ship_id")
    print("3. storage_zone_id")
    opt = int(input(":"))
    if opt == 1:
        weight = float(input("Weight :"))
        Container.update_by_id(id=id, weight=weight)
        success_msg(f"container updated successfully for id {id}")
    elif opt == 2:
        ship_id = int(input("ship id :"))
        Container.update_by_id(id=id, ship_id=ship_id)
        success_msg(f"container updated successfully for id {id}")
    elif opt == 3:
        storage_zone_id = int(input("storage zone id :"))
        Container.update_by_id(id=id, storage_zone_id=storage_zone_id)
        success_msg(f"container updated successfully for id {id}")
    else:
        warning_msg("Invalid Option!")

def delete_container():
    clear_console()
    containers = Container.get()
    print("-"*58)
    print("|    id    |    weight    |  storage_zone_id |  ship_id  |")
    print("-"*58)
    for container in containers:
        show_container_data(container)
    print("-"*58)

    id = int(input("Enter id to delete :"))
    opt = input(f"Are you sure you want to delete container with id {id} (y/n) :")

    if opt == 'y' or opt == 'Y':
        Container.delete_by_id(id=id)
        success_msg("Container deleted successfully!")
    elif opt == 'n' or opt == 'N':
        warning_msg("Canceled by user!")
    else:
        warning_msg("Invalid Option!")