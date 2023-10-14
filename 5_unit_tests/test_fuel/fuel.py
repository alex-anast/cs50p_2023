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
    percentage = convert(input())
    print(gauge(percentage))


def convert(fraction: str = "") -> int:
    # force input to be X/Y
    if "/" in fraction:
        fraction = fraction.split("/")
    else:
        raise ValueError
    X = int(fraction[0])
    Y = int(fraction[1])
    if Y == 0:
        raise ZeroDivisionError
    elif X > Y:
        raise ValueError
    else:
        return int(round(float(X / Y), 2) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
