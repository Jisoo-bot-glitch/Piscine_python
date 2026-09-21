class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = round(height + 0.0, 1)
        self.plant_age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def plant_factory() -> None:
    plant1 = Plant("rose", 25, 30)
    print("=== Plant Factory Output ===")
    print("Created: ", end=" ")
    plant1.show()
    plant2 = Plant("oak", 200, 365)
    print("Created: ", end=" ")
    plant2.show()
    plant3 = Plant("cactus", 5, 90)
    print("Created: ", end=" ")
    plant3.show()
    plant4 = Plant("sunflower", 80, 45)
    print("Created: ", end=" ")
    plant4.show()
    plant5 = Plant("fern", 15, 120)
    print("Created: ", end=" ")
    plant5.show()


def main() -> None:
    plant_factory()


if __name__ == "__main__":
    main()
