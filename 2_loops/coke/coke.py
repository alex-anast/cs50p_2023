"""
Suppose that a machine sells bottles of Coca-Cola for 50 cents
and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

Implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.

Once the user has inputted at least 50 cents,
output how many cents in change the user is owed.

Assume that the user will only input integers,
and ignore any integer that isn't an accepted denomination.
"""

COLA_PRICE_CENTS = 50


def main():
    debt = COLA_PRICE_CENTS
    while True:
        print(f"Amount Due: {debt}")
        user_coin = int(input("Insert Coin: "))

        # check for correct user input
        if user_coin not in [5, 10, 25]:
            continue

        debt -= user_coin
        if debt <= 0:
            print(f"Change Owed: {abs(debt)}")
            break


if __name__ == "__main__":
    main()
