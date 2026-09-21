#!usr/bin/python3
import random

achievements_list: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"
]


def gen_player_achievements() -> set[str]:
    random_number = random.randint(1, len(achievements_list))
    achievements = random.sample(achievements_list, k=random_number)
    return set(achievements)


if __name__ == "__main__":
    Full_list = set(achievements_list)
    Player_Alice = gen_player_achievements()
    Player_Bob = gen_player_achievements()
    Player_Charlie = gen_player_achievements()
    Player_Dylan = gen_player_achievements()
    all_dist = Player_Alice.union(Player_Bob, Player_Charlie, Player_Dylan)
    com = Player_Alice.intersection(Player_Bob, Player_Charlie, Player_Dylan)
    Only_A = Player_Alice.difference(Player_Bob, Player_Charlie, Player_Dylan)
    Only_B = Player_Bob.difference(Player_Alice, Player_Charlie, Player_Dylan)
    Only_C = Player_Charlie.difference(Player_Bob, Player_Alice, Player_Dylan)
    Only_D = Player_Dylan.difference(Player_Bob, Player_Alice, Player_Charlie)
    Alice_is_missing = Full_list.difference(Player_Alice)
    Bob_is_missing = Full_list.difference(Player_Bob)
    Charlie_is_missing = Full_list - Player_Charlie
    Dylan_is_missing = Full_list - Player_Dylan
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {Player_Alice}")
    print(f"Player Bob: {Player_Bob}")
    print(f"Player Charlie: {Player_Charlie}")
    print(f"Player Dylan: {Player_Dylan}\n")
    print(f"All distinct achievements: {all_dist}\n")
    print(f"Common achievements: {com}\n")
    print(f"Only Alice has: {Only_A}")
    print(f"Only Bob has: {Only_B}")
    print(f"Only Charlie has: {Only_C}")
    print(f"Only Dylan has: {Only_D}\n")
    print(f"Alice is missing: {Alice_is_missing}")
    print(f"Bob is missing: {Bob_is_missing}")
    print(f"Charlie is missing: {Charlie_is_missing}")
    print(f"Dylan is missing: {Dylan_is_missing}")
