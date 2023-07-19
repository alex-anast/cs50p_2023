"""
Implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or
(case-insensitively) forty-two or forty two. Otherwise output No.
"""


def main():
    query = input("What is the greatest Question of Life? ").lower().strip()
    match query:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


if __name__ == "__main__":
    main()
