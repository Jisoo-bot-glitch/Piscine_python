def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "string" + 123
    return (operation_number)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation in range(5):
        print(f"Testing operation {operation}...")

        try:
            garden_operations(operation)

        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")

        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
