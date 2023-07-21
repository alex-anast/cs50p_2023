"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates
that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

Implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank
is essentially empty. And if 99% or more remains, output F instead to indicate
that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
instead prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""


def main():
    fraction_percentage = get_fraction_percentage()
    if fraction_percentage <= 1:
        print("E")
    elif fraction_percentage >= 99:
        print("F")
    else:
        print(f"{fraction_percentage:.0f}%")


def get_fraction_percentage():
    while True:
        user_input = input("Fraction: ")
        user_input = user_input.split("/")
        if len(user_input) == 2:
            try:
                numerator = int(user_input[0])
                denominator = int(user_input[1])
                if numerator > denominator:
                    continue
                return round(float(numerator / denominator), 2) * 100
            except ValueError as err:
                print(f"ValueError: {err}")
            except ZeroDivisionError as err:
                print(f"ZeroDivisionError: {err}")


if __name__ == "__main__":
    main()
