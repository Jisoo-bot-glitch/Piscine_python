#!usr/bin/python3
import sys
my_inventory = {}
print("=== Inventory System Analysis ===")
for argv in sys.argv[1:]:
    parts = argv.split(':')
    try:
        if parts[0] in my_inventory:
            print(f"Redundant item ’{parts[0]}’ - discarding")
        else:
            my_inventory[str(parts[0])] = int(parts[1])
    except IndexError:
        print(f'Error - invalid parameter: ’{parts[0]}’')
    except ValueError as e:
        print(f'Quantity error for ’{parts[0]}’: {e}')

if __name__ == "__main__":
    print("Got inventory:", my_inventory)
    print("Item list:", list(my_inventory.keys()))
    print("Total quantity of the", len(my_inventory.values()), end="")
    print(" items:", sum(my_inventory.values()))
    big_name = None
    small_name = None
    big_qty = -1
    small_qty = 100
    for name, qty in my_inventory.items():
        if big_qty < qty:
            big_qty = qty
            big_name = name
        if small_qty > qty:
            small_qty = qty
            small_name = name
        print(f"Item {name} represents ", end="")
        print(f"{round((qty/sum(my_inventory.values())*100), 1)}%")
    print(f"Item most abundant: {big_name} with quantity {big_qty}")
    print(f"Item least abundant: {small_name} with quantity {small_qty}")
    my_inventory2 = {
        "sword": 1,
        "potion": 5,
        "shield": 2,
        "armor": 3,
        "helmet": 1,
        "magic_item": 1
    }
    my_inventory.update(my_inventory2)
    print("Updated inventory:", my_inventory)
