"""
In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones.
Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

Implement a program that prompts the user for a vanity plate
and then output Valid if meets all of the requirements
or Invalid if it does not.

Assume that any letters in the user's input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""

import string


def main():
    user_plate = input("Input vanity plate: ")
    if is_valid(user_plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate: str = "") -> bool:
    if (
        check_minMax(plate)
        and check_start(plate)
        and check_numbersInMiddle(plate)
        and check_specialChars(plate)
    ):
        return True
    else:
        return False


# All vanity plates must start with at least two letters.
def check_start(plate: str) -> bool:
    return plate[0].isalpha() and plate[1].isalpha()


# vanity plates may contain a max 6 chars and min 2 chars.
def check_minMax(plate: str) -> bool:
    return 2 <= len(plate) <= 6


# Numbers cannot be used in the middle of a plate; they must come at the end.
def check_numbersInMiddle(plate: str) -> bool:
    found_number = False
    for element in plate:
        if element.isdigit():
            if found_number is False:
                # the first number can't be 0
                if element == "0":
                    return False
                found_number = True
        # if number has already been found, return Invalid if letter is found
        if found_number and element.isalpha():
            return False
    return True


# No periods, spaces, or punctuation marks are allowed.
def check_specialChars(plate: str) -> bool:
    for letter in plate:
        if letter in string.punctuation or letter == " ":
            return False
    return True


if __name__ == "__main__":
    main()
