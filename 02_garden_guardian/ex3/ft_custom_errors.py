class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(
        self,
        name: str = "plant",
        state: str = "unknown"
    ) -> None:
        super().__init__(
            f" The {name} plant is {state}!"
        )


class WaterError(GardenError):
    def __init__(self, where: str = "unknown") -> None:
        super().__init__(
            f" Not enough water in the {where}!"
        )


def garden_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        raise PlantError("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        raise WaterError("tank")
    except WaterError as e:
        print(f"Caught WaterError:{e}")
    try:
        print("\nTesting catching all garden errors...")
        raise PlantError("tomato", "wilting")
    except GardenError as e:
        print(f"Caught GardenError:{e}")
    try:
        raise WaterError("tank")
    except GardenError as e:
        print(f"Caught GardenError:{e}")
    finally:
        print("\nAll custom error types work correctly!")


def main() -> None:
    garden_error_types()


if __name__ == "__main__":
    main()
