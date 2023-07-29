"""
One way to measure the complexity of a program is to count
its number of lines of code (LOC), excluding blanks and comments.
Of course, just because a program (or even function) has more lines
of code than another doesn't necessarily mean it's more complex

Implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines
of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument,
or if the specified file's name does not end in .py,
or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace,
is a comment. (A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
"""


import sys
import os


def main():
    filename = cli_input()
    no_lines = getNoLOF(filename)
    print(no_lines)


def cli_input() -> str:
    # if exactly one argument or name exists or name ends with .py
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
    else:
        return sys.argv[1]


def getNoLOF(filename: str = "") -> int:
    with open(filename) as file:
        rows = file.readlines()
    line_counter = 0
    for row in rows:
        row = row.strip()
        # remove whitespace
        if len(row) == 0 or row[0] == "#":
            continue
        else:
            line_counter += 1
    return line_counter


if __name__ == "__main__":
    main()
