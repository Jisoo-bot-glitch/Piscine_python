import sys
import typing

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        try:
            print(f"Accessing file ’{sys.argv[1]}’")
            f: typing.IO[str] = open(sys.argv[1], "r")
        except IOError as e:
            print(f"Error opening file ’{sys.argv[1]}’: {e}")
        else:
            print("---\n")
            lines = f.read()
            for line in lines:
                print(line, end="")
            print("\n---")
            f.close()
            print(f"File ’{sys.argv[1]}’ closed.")
