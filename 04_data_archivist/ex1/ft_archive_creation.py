import sys
import typing

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
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
            print()
            print("\n---")
            f.close()
            print(f"File ’{sys.argv[1]}’ closed.\n")
            print("Transform data:")
            print("---\n")
            lines_split = lines.split("\n")
            new_content = ""
            for line in lines_split:
                new_content = new_content + line + "#" + "\n"
            print(new_content, end="")
            print("\n---")
            name = input("Enter new file name (or empty):  ")
            if name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to ’{name}’")
                new_f = open(name, "w")
                new_f.write(new_content)
                new_f.close()
                print(f"Data saved in file ’{name}’.")
