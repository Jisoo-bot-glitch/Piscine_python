#!usr/bin/python3
import math
print("=== Game Coordinate System ===\n")


def get_player_pos(put_any: bool) -> tuple[float, float, float]:
    while True:
        answer = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = answer.split(',')
        values = []
        for part in parts:
            try:
                values.append(float(part))
            except ValueError as e:
                if put_any:
                    print('Invalid syntax')
                else:
                    print(f"Error on parameter '{part}': {e}")
                break
        else:
            if len(values) == 3:
                return (values[0], values[1], values[2])
            else:
                print('Invalid syntax')


print("Get a first set of coordinates")
coords = get_player_pos(True)
d = round(math.sqrt((coords[0]-0)**2 + (coords[1]-0)**2 + (coords[2]-0)**2), 4)
print(f'Got a first tuple: {coords}')
print(f'It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}')
print(f'Distance to center: {d}')
print("\nGet a second set of coordinates")
coords2 = get_player_pos(False)
dx = coords[0]-coords2[0]
dy = coords[1]-coords2[1]
dz = coords[2]-coords2[2]
d2 = round(math.sqrt(dx**2 + dy**2 + dz**2), 4)
print(f'Distance between the 2 sets of coordinates: {d2}')
