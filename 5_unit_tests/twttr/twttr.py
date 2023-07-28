"""
The problem has been implemented in the set of week2.
The concept now is to write the code in a way
that it is easily tested.

Best practices, to create functions that return
something specific. Make the code modular.
"""


def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(user_input: str) -> str:
    for letter in user_input:
        if letter in "aAeEiIoOuU":
            user_input = user_input.replace(letter, "")
    return str(user_input)


if __name__ == "__main__":
    main()
