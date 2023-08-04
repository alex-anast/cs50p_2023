"""
When creating a Google Form that prompts users for a short answer
(or paragraph), it's possible to enable response validation and
require that the user's input match a regular expression.
For instance, you could require that a user input an
email address with a regex like this one:

^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-] \
{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

Or you could more easily use Google's built-in support
for validating an email address.

Using either validator-collection or validators from PyPI,
implement a program that prompts the user for an email address
via input and then prints Valid or Invalid, respectively,
if the input is a syntactically valid email address.
You may not use re. And do not validate whether
the email address's domain name actually exists.
"""


from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(email_address: str) -> str:
    return "Valid" if checkers.is_email(email_address) else "Invalid"


if __name__ == "__main__":
    main()
