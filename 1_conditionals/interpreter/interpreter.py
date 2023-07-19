"""
Implement a program that prompts the user for an arithmetic expression
and then calculates and outputs the result as a floating-point value
formatted to one decimal place.

Assume that the user's input will be formatted as x y z,
with one space between x and y and one space between y and z, wherein:

- x is an integer
- y is +, -, *, or /
- z is an integer
"""


def main():
    user_input = input("Equation: ").split()
    operation = user_input[1]
    match operation:
        case "+":
            print("{:.1f}".format(int(user_input[0]) + int(user_input[2])))
        case "-":
            print("{:.1f}".format(int(user_input[0]) - int(user_input[2])))
        case "*":
            print("{:.1f}".format(int(user_input[0]) * int(user_input[2])))
        case "/":
            print("{:.1f}".format(int(user_input[0]) / int(user_input[2])))


if __name__ == "__main__":
    main()
