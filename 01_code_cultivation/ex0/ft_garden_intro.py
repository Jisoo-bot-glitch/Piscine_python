def my_garden() -> None:
    plant_name = "Rose"
    plant_height = 25
    plant_age = 30
    print(f'Plant: {plant_name}')
    print(f'Height: {plant_height}cm')
    print(f'Age: {plant_age} days')


def main() -> None:
    print('=== Welcome to My Garden ===')
    my_garden()
    print('\n=== End of Program ===')


if __name__ == "__main__":
    main()
