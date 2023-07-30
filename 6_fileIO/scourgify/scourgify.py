"""
Data, too, often needs to be “cleaned,” as by reformatting it,
so that values are in a consistent, if not more convenient, format. 

DoD: Implement a program that:

1. Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input,
      whose columns are assumed to be, in order, name and house, and
    - the name of a new CSV to write as output,
      whose columns should be, in order, first, last, and house.
2. Converts that input to that output, splitting each name into
   a first name and last name. Assume that each student will have
   both a first name and last name.

If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via sys.exit
with an error message.
"""


import sys
import os
import csv


def main():
    csv_in, csv_out = getCSVNames()
    # for the future: it would be nice to be done in place so that
    # it doesn't load up the RAM. Maybe a kind of generator and yield?
    first_name, last_name, house = customCSVConvert(csv_in)
    putCSVData(csv_out, first_name, last_name, house)


def getCSVNames() -> list:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        return [sys.argv[1], sys.argv[2]]


def customCSVConvert(csv_in) -> list:
    first_name = []
    last_name = []
    house = []
    with open(csv_in, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            house.append(row["house"])
            name_list = []  # I don't know if I need that
            name_list = row["name"].split(",")
            # comes with a space in front
            first_name.append(name_list[1].strip())
            last_name.append(name_list[0])
    return [first_name, last_name, house]


def putCSVData(csv_out, first_name, last_name, house) -> None:
    with open(csv_out, "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "first name",
                "last name",
                "house",
            ],
        )
        writer.writeheader()
        for i in range(len(first_name)):
            writer.writerow(
                {
                    "first name": first_name[i],
                    "last name": last_name[i],
                    "house": house[i],
                }
            )


if __name__ == "__main__":
    main()
