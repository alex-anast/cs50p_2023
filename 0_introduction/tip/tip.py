'''
* dollars_to_float, format $##.##, wherein each # is a decimal digit
* percent_to_float, format ##%, wherein each # is a decimal digit
'''

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
def dollars_to_float(d) -> float:
    return round(float(d[1:]), 2)


# remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
def percent_to_float(p) -> float:
    return float(p[:-1]) / 100


if __name__ == '__main__':
    main()
