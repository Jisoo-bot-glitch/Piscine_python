import elements as ele
from alchemy import elements as ale


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"’{ale.create_earth()}’ and ’{ale.create_air()}’")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"’{ele.create_fire()}’ and ’{ele.create_water()}’")
