import random

player_name = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
]
cap_names = [name.capitalize() for name in player_name]
origin_cap_name = [name for name in player_name if name[0].isupper()]
sco = {name: random.randint(1, 999) for name in cap_names}
average = round(sum(sco.values())/len(sco.values()), 2)
higher_av = {name: sco[name] for name in sco if sco[name] > average}
if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print("Initial list of players:", player_name)
    print("New list with all names capitalized: ", cap_names)
    print("New list of capitalized names only: ", origin_cap_name)
    print("\nScore dict:", sco)
    print(f"Score average is {average}")
    print("High scores:", higher_av)
