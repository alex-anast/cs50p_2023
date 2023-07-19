"""
In some languages, it's common to use camel case (otherwise known as “mixed case”) for variables' names
when those names comprise multiple words,
whereby the first letter of the first word is lowercase but the first letter of each subsequent word
is uppercase.

Python, by contrast, recommends snake case, whereby words are instead separated
by underscores (_), with all letters in lowercase.

Implement a program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case.
"""


def main():
    user_input = input("Give something in camelCase: ")
    print(f"camelCase: {user_input}")
    user_input = snakeCase_convert(user_input)
    print(f"snake_case: {user_input}")


def snakeCase_convert(word: str) -> str:
    for i, letter in enumerate(word):
        if letter.isupper():
            word = word.replace(letter, "_" + letter.lower())
    return word


if __name__ == "__main__":
    main()
