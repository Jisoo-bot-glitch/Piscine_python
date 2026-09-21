def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return (temp_int)


def test_temperature(temp_str: str) -> None:
    try:
        input_temperature(temp_str)
    except ValueError as e:
        print(f"\nInput data is ’{temp_str}’")
        print(f"Caught input_temperature error: {e}")
    else:
        print(f"\nInput data is ’{temp_str}’")
        print(f"Temperature is now {temp_str}°C")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    main()
