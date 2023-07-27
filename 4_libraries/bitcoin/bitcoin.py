"""
Implement a program that:

- Expects the user to specify as a command-line argument
  the number of Bitcoins, n, that they would like to buy.
  If that argument cannot be converted to a float,
  the program should exit via sys.exit with an error message.

- Queries the API for the CoinDesk Bitcoin Price Index at
  https://api.coindesk.com/v1/bpi/currentprice.json,
  which returns a JSON object, among whose nested keys
  is the current price of Bitcoin as a float.

- Outputs the current cost of Bitcoins in USD to
  four decimal places, using , as a thousands separator.
"""

import requests
import sys


def main():
    number_of_bitcoins = getUserInput()
    try:
        coindesk_bitcoin_price = getBitcoinPrice()
    except:
        print("wtf 2")
    print(calculatePrice(number_of_bitcoins, coindesk_bitcoin_price))


def getUserInput() -> float:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Too many arguments")


def getBitcoinPrice(
    input_url: str = "https://api.coindesk.com/v1/bpi/currentprice.json",
) -> float:
    try:
        response = requests.get(url=input_url)
        return response.json()["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("URL response error")


def calculatePrice(price: float, bitcoins: float = 1) -> str:
    total_price = price * bitcoins
    return f"${total_price:,.4f}"


if __name__ == "__main__":
    main()
