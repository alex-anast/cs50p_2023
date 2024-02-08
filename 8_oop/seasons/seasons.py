# season.py

"""
Implement a program that prompts the user for their date of birth
in YYYY-MM-DD format and then sings prints how old they are
in minutes, rounded to the nearest integer, using English words
instead of numerals, just like the song from Rent, without any
and between words. Since a user might not know the time at which
they were born, assume, for simplicity, that the user was born
at midnight (i.e., 00:00:00) on that date. And assume that
the current time is also midnight. In other words, even if
the user runs the program at noon, assume that it's actually
midnight, on the same date.

You're welcome to import other (built-in) libraries, or any
that are specified in the below hints. Exit via sys.exit
if the user does not input a date in YYYY-MM-DD format.
Ensure that your program will not raise any exceptions.
"""


import sys
import inflect
from typing import Optional
from datetime import date


def main():
    print(convert_to_seconds(dob=input("Date of Birth: ")))


def convert_to_seconds(dob: str = "", dt: Optional[str] = None) -> str:
    """
    Convert the difference between a given date and the date of birth into seconds.

    This function first validates the input date of birth. If the input is invalid, it will exit the program with an error message.
    It then calculates the difference between the current date (or a given date) and the date of birth. The difference is returned as a string in seconds.

    Args:
        dob (str): The date of birth to calculate the difference from. It should be in the format "YYYY-MM-DD".
        dt (Optional[str]): The date to calculate the difference to. If not provided, the current date is used. It should be in the format "YYYY-MM-DD".

    Returns:
        str: The difference between the two dates in seconds, converted into words.
    """
    try:
        check_input(dob)
    except ValueError as ve:
        sys.exit(ve)
    except TypeError as te:
        sys.exit(te)
    except:
        sys.exit("Unknown Error")

    # handle whether it's relative to today or not
    if dt is None:
        dt = date.today()
    else:
        test_dt = dt.split("-")
        dt = date(int(test_dt[0]), int(test_dt[1]), int(test_dt[2]))

    # coming in as i.e. 1999-12-31
    dob = dob.split("-")
    epoch_time = date(int(dob[0]), int(dob[1]), int(dob[2]))
    # use of sub operator, overloads and returns datetime object
    delta = (dt - epoch_time) / 60  # gives back minutes
    return f"{num2words(delta.total_seconds())} minutes"


def num2words(number: int) -> str:
    """
    Convert a number into its words representation.

    This function uses the inflect library to convert a number into words.
    It removes the 'and' word from the representation and capitalizes the first letter.

    Args:
        number (int): The number to convert.

    Returns:
        str: The words representation of the number.
    """
    # Use inflect engine to convert minutes to words
    p = inflect.engine()
    words_representation = p.number_to_words(int(number), andword="")
    # capitalize first word and reformat ending
    return words_representation.capitalize()


def check_input(dob: str) -> bool:
    """
    Validate the input date of birth string.

    This function checks if the input is a string and if it follows the correct format (YYYY-MM-DD).
    It raises a TypeError if the input is not a string, a ValueError if the input does not contain a "-" character,
    and another ValueError if the input does not contain three elements when split by "-".

    Args:
        dob (str): The date of birth to validate.

    Returns:
        bool: True if the input is valid, otherwise it raises an error.
    """
    # check type
    if not isinstance(dob, str):
        raise TypeError("TypeError: input is not a string")
    if "-" not in dob:
        raise ValueError('ValueError: input missing "-" char')
    temp = dob.split("-")
    if not len(temp) == 3:
        raise ValueError("ValueError: input missing year, month or/and day")
    return True


if __name__ == "__main__":
    main()
