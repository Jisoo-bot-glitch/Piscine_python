def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return (temp_int)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    try:
        inp = input_temperature("25")
    except ValueError as e:
        print(f"\nInput data is ’{inp}’")
        print(f"Caught input_temperature error: {e}")
    else:
        print(f"\nInput data is ’{inp}’")
        print(f"Temperature is now {inp}°C")
    try:
        input_temperature("abc")
    except ValueError as e:
        print("\nInput data is ’abc’")
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("100")
    except ValueError as e:
        print("\nInput data is ’100’")
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("-50")
    except ValueError as e:
        print("\nInput data is ’-50’")
        print(f"Caught input_temperature error: {e}")
    finally:
        print("\nAll tests completed - program didn’t crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
