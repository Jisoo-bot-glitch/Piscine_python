class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = round(height + 0.0, 1)
        self._plant_age = age
        self._stats = Plant.Stats(self._name)

    @staticmethod
    def older_than_year(age: int) -> bool:
        return age >= 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return Plant("Unknown plant", 0, 0)

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
        self._height = round(self._height + 0.8, 1)
        self._stats._grow_count += 1

    def age(self) -> None:
        self._plant_age += 1
        self._stats._age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._plant_age} days old")
        self._stats._show_count += 1

    class Stats:
        def __init__(self, name: str) -> None:
            self._name = name
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._count_shade = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, ", end="")
            print(f"{self._age_count} age, {self._show_count} show")


class Flower(Plant):
    def __init__(self, color: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def grow(self) -> None:
        self._height = round(self._height + 8, 1)
        self._stats._grow_count += 1

    def bloom(self) -> None:
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
            self._is_blooming = True


class Seed(Flower):
    def __init__(self, color: str, name: str, height: int, age: int) -> None:
        super().__init__(color, name, height, age)
        self._is_blooming = False
        self._seeds = 0

    def show(self) -> None:
        super().show()

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 1)
        self._stats._grow_count += 1

    def age(self) -> None:
        self._plant_age += 20
        self._stats._age_count += 1

    def bloom(self) -> None:
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
            print(f"Seeds: {self._seeds}")
        else:
            print(f"{self._name} has not bloomed yet")
            print(f"Seeds: {self._seeds}")
            self._is_blooming = True
            self._seeds = 42


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
        self._stats._count_shade = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        if not self._is_shade:
            self._is_shade = True
            self._stats._count_shade += 1
            print(f"Tree {self._name} now produces a shade of ", end="")
            print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def display_shade(self) -> None:
        self._stats.display()
        print(f"{self._stats._count_shade} shade")


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

        if self.plant_age < 20:
            print(f"[make {self._name.lower()} grow and age for 20 days]")


def garden_analytic() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")
    print()
    print("=== Flower")
    plant1 = Flower("red", "rose", 15, 10)
    plant1.show()
    plant1.bloom()
    print(f"[statistics for {plant1._name}]")
    display_stats(plant1)
    print(f"[asking the {plant1._name.lower()} to grow and bloom]")
    plant1.grow()
    plant1.show()
    plant1.bloom()
    print(f"[statistics for {plant1._name}]")
    display_stats(plant1)
    print("\n=== Tree")
    plant2 = Tree(5, "oak", 200, 365)
    plant2.show()
    print(f"[statistics for {plant2._name}]")
    plant2.display_shade()
    print(f"[asking the {plant2._name.lower()} to produce shade]")
    plant2.produce_shade()
    print(f"[statistics for {plant2._name}]")
    plant2.display_shade()
    print("\n=== Seed")
    plant3 = Seed("yellow", "Sunflower", 80, 45)
    plant3.show()
    plant3.bloom()
    print(f"[make {plant3._name.lower()} grow, age and bloom]")
    plant3.grow()
    plant3.age()
    plant3.show()
    plant3.bloom()
    print(f"[statistics for {plant3._name}]")
    display_stats(plant3)
    print("\n=== Anonymous")
    plant4 = Plant("Unknown plant", 0, 0).make_anonymous()
    plant4.show()
    print(f"[statistics for {plant4._name}]")
    display_stats(plant4)


def display_stats(plant: Plant) -> None:
    plant._stats.display()


def main() -> None:
    garden_analytic()


if __name__ == "__main__":
    main()
