"""
Implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100.
Ignore any leading whitespace in the user's greeting,
and treat the user's greeting case-insensitively.
"""


def main():
    greeting = input("What is your greeting? ")
    print(value(greeting))


def value(greeting: str = "") -> int:
    greeting = greeting.lower().strip()
    if len(greeting) == 0:
        return 100
    else:
        if greeting[:5] == "hello":
            return 0
        elif greeting[0] == "h":
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()
