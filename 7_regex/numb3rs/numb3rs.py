"""
Implement a function called validate that expects an IPv4 address
as input as a str and then returns True or False, respectively,
if that input is a valid IPv4 address or not.

Additionally implement two or more functions that collectively
test your implementation of validate thoroughly.
"""


import re
import sys


def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except:
        sys.exit("Exited with error.")


def validate(ip):
    # match the range 0-255 four times with a dot in-between
    is_valid = re.search(
        r"^(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\."
        + r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\."
        + r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\."
        + r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)$",
        ip,
    )
    if is_valid:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
