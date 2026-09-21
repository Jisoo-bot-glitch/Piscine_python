import elements
from alchemy.potions import strength_potion


from ..elements import create_air


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: "
            f"brew ’{create_air()}’ and ’{strength_potion()}’"
            f" mixed with ’{elements.create_fire()}’")
