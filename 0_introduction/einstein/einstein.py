'''
E = m c^2, wherein
E: represents energy (measured in Joules),
m: represents mass (measured in kilograms), and
c: represents the speed of light (measured approximately as 300,000 km per second),
per Albert Einstein et al. The formula means that mass and energy are equivalent.

Implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
'''

def main():
    mass = int(input("Type mass as integer (in kilograms): "))
    print(einstein_formula(mass))


def einstein_formula(mass: int) -> int:
    return mass * pow(3 * pow(10, 8), 2)


if __name__ == '__main__':
    main()
