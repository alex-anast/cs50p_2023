"""
Implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio's format (a restaurant),
and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate.

Format the table using the library's grid format.
If the user does not specify exactly one command-line argument,
or if the specified file's name does not end in .csv,
or if the specified file does not exist,
the program should instead exit via sys.exit.
"""


import sys

sys.path.append("..")  # add the parent dir to sys.path


from lines.lines import cli_input
import csv
from tabulate import tabulate


def main():
    filename = cli_input(file_extension=".csv")
    with open(filename) as f:
        rows = csv.reader(f)
        rows_list = []
        for row in rows:
            rows_list.append(row)
        headers = rows_list[0]
        print(tabulate(rows_list[1:], headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
