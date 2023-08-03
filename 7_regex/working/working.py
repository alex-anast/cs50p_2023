"""
Implement a function called convert that expects a str in either
of the 12-hour formats below and returns the corresponding str
in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein)
and that there will be a space before each.
Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM specifically.

- 9:00 AM to 5:00 PM
- 9 AM to 5 PM

Raise a ValueError instead if the input to convert is not
in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.).
But do not assume that someone's hours will start ante meridiem
and end post meridiem; someone might work late and even long hours
(e.g., 5:00 PM to 9:00 AM).
"""


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = check_input(s).split(" ")
    return convert_hour(s[0], s[1]) + " to " + convert_hour(s[3], s[4])


def convert_hour(time: str, period: str) -> str:
    # fix the hours
    hours = int(time.split(":")[0]) if ":" in time else int(time)
    hours = hours + 12 if period == "PM" else hours
    hours = "0" if hours == 12 and period == "AM" else hours
    hours = "12" if hours == 24 and period == "PM" else str(hours)
    hours = f"0{hours}" if len(hours) == 1 else hours

    # check if the minutes are specified and return appropriately
    minutes = time.split(":")[1] if ":" in time else None
    return f"{hours}:{minutes}" if minutes else f"{hours}:00"


def check_input(user_input, question: str = "Hours: ") -> str:
    user_input = user_input.strip().split(" ")
    # check length of input or if keywords exist
    if len(user_input) == 5 and (
        user_input[1] in ["AM", "PM"]
        and user_input[2] == "to"
        and user_input[4] in ["AM", "PM"]
    ):
        # check if format of numbers is correct
        pattern1 = (
            r"^(1[0-2]|[1-9]):(?:[0-5][0-9])$"
            if ":" in user_input[0]
            else r"^(1[0-2]|[1-9])$"
        )
        pattern2 = (
            r"^(1[0-2]|[1-9]):(?:[0-5][0-9])$"
            if ":" in user_input[3]
            else r"^(1[0-2]|[1-9])$"
        )
        matches1 = re.search(pattern=pattern1, string=user_input[0])
        matches2 = re.search(pattern=pattern2, string=user_input[3])
        if matches1 and matches2:
            return " ".join(user_input)
    raise ValueError


if __name__ == "__main__":
    main()
