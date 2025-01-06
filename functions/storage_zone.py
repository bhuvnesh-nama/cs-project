# Functions For Storage Zone Management
from db.models import StorageZone
from helper import *

# To Add New Storage Zone
def add_new_storage_zone():
    clear_console()
    name = input("Name :").upper()
    max_capacity = int(input("Max Capacity (in containers) :"))

    already_exists = StorageZone.get(name=name)

    if already_exists:
        warning_msg("Container Alreary Exists")
        input("Enter to quit:")
        return
    
    storage_zone = StorageZone(name=name, max_capacity=max_capacity)
    storage_zone.save()

    success_msg("Storage zone addedd successfully")

# To Get All Storage Zones
def get_all_storage_zone():
    clear_console()
    storage_zones = StorageZone.get()
    print("-" * 46)
    print("|     id     |     name     |  max capacity  |")
    print("-" * 46)
    for storage_zone in storage_zones:
        show_storage_zone_data(storage_zone)
    print("-" * 46)
    input("Enter to quit :")

# To Update Storage Zone
def update_storage_zone():
    clear_console()
    storage_zones = StorageZone.get()
    print("-" * 46)
    print("|     id     |     name     |  max capacity  |")
    print("-" * 46)
    for storage_zone in storage_zones:
        show_storage_zone_data(storage_zone)
    print("-" * 46)

    id = int(input("Enter id to update :"))
    print()
    print("What you want to update?")
    print("1. Name")
    print("2. Max Capacity")
    opt = int(input(":"))
    if opt == 1:
        name = input("Name :")
        StorageZone.update_by_id(id=id,name=name)
    elif opt ==2:
        max_capacity = int(input("Max Capacity (in containers) :"))
        StorageZone.update_by_id(id=id, max_capacity=max_capacity)
    else:
        warning_msg("Invalid Option!")

# To Delete Storage Zone
def delete_storage_zone():
    clear_console()
    storage_zones = StorageZone.get()
    print("-" * 46)
    print("|     id     |     name     |  max capacity  |")
    print("-" * 46)
    for storage_zone in storage_zones:
        show_storage_zone_data(storage_zone)
    print("-" * 46)

    id = int(input("Enter id:"))
    opt = input(f"Are you sure you want to delete storage zone with id {id} (y/n) :")
    if opt == 'y' or opt == 'Y':
        StorageZone.delete_by_id(id=id)
    else:
        warning_msg("Cancelled by user")