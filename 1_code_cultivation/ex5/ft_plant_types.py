class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = round(height + 0.0, 1)
        self._plant_age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def set_height(self, height: int) -> None:
        if height > 0:
            self.height = round(height + 0.0, 1)
            print(f"Height updated: {height}cm")

        else:
            print(f"{self._name}: Error, height can’t be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self.plant_age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can’t be negative")
            print("Age update rejected")

    def grow(self) -> None:
        self._height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self._plant_age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._plant_age} days old")


class Flower(Plant):
    def __init__(self, color: str, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def bloom(self) -> None:
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
            print(f"[asking the {self._name.lower()} to bloom]")
            self._is_blooming = True


class Tree(Plant):
    def __init__(
        self,
        diameter: int,
        name: str,
        height: int,
        age: int
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = round(diameter + 0.0, 1)
        self._is_shade = False

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")
        self._is_shade = False

    def produce_shade(self) -> None:
        if self._is_shade:
            print(f"Tree {self._name} now produces a shade of ", end="")
            print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        else:
            print(f"[asking the {self._name.lower()} to produce shade]")
            self._is_shade = True


class Vegetable(Plant):
    def __init__(
        self,
        season: str,
        value: int,
        name: str,
        height: int,
        age: int
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = season
        self._nu_value = value

    def grow(self) -> None:
        super().grow()
        self._nu_value += 1

    def age(self) -> None:
        super().age()
        self._nu_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nu_value}")

        if self._plant_age < 20:
            print(f"[make {self._name.lower()} grow and age for 20 days]")


def plant_type() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("red", "rose", 15, 10)
    plant1.show()
    plant1.bloom()
    plant1.show()
    plant1.bloom()
    print("\n=== Tree")
    plant2 = Tree(5, "oak", 200, 365)
    plant2.show()
    plant2.produce_shade()
    plant2.produce_shade()
    print("\n=== Vegetable")
    plant3 = Vegetable("April", 0, "tomato", 5, 10)
    plant3.show()
    plant3 = Vegetable("April", 20, "tomato", 47, 30)
    plant3.show()


def main() -> None:
    plant_type()


if __name__ == "__main__":
    main()
