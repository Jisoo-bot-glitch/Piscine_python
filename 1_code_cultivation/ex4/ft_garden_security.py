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
            self._height = round(height + 0.0, 1)
            print(f"Height updated: {height}cm")

        else:
            print(f"{self._name}: Error, height can’t be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self._plant_age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can’t be negative")
            print("Age update rejected")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._plant_age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._plant_age} days old")


def plant_factory() -> None:
    plant1 = Plant("rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end=" ")
    plant1.show()
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-1)
    plant1.set_age(-2)
    print()
    print("Current state: ", end=" ")
    plant1.show()


def main() -> None:
    plant_factory()


if __name__ == "__main__":
    main()
