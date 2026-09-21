class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = round(height + 0.0, 1)
        self.start_height = height
        self.plant_age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def garden_growth() -> None:
    plant1 = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print("Growth this week: ", end="")
    print(f"{round(plant1.height - plant1.start_height, 1)}cm")


def main() -> None:
    garden_growth()


if __name__ == "__main__":
    main()
