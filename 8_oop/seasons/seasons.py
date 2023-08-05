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


from datetime import date
import sys
import inflect


def main():
    print(convert_to_seconds(dob=input("Date of Birth: ")))


def convert_to_seconds(dob="", dt=None) -> str:
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


def num2words(number) -> str:
    # Use inflect engine to convert minutes to words
    p = inflect.engine()
    words_representation = p.number_to_words(int(number), andword="")
    # capitalize first word and reformat ending
    return words_representation.capitalize()


def check_input(dob) -> bool:
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
