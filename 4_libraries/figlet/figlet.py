"""
FIGlet, named after Frank, Ian, and Glen's letters,
is a program from the early 1990s for making large
letters out of ordinary text, a form of ASCII art.

Implement a program that:

- Expects zero or two command-line arguments:
- Zero if the user would like to output text in a random font.
- Two if the user would like to output text in a specific font,
  in which case the first of the two should be -f or --font,
  and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first
  is not -f or --font or the second is not the name of a font,
  the program should exit via sys.exit with an error message.
"""

import sys
import pyfiglet
import random


# this exercise is about the cli arguments
def main():
    font_generic_object = pyfiglet.FigletFont

    # filename is always the first
    if len(sys.argv[1:]) == 0:
        # random font
        user_font = random.choice(font_generic_object.getFonts())
    elif (
        len(sys.argv[1:]) == 2
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in font_generic_object.getFonts()
    ):
        # specific font
        user_font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    user_text = input("Input: ")
    user_figlet = pyfiglet.Figlet(font=user_font)
    print(user_figlet.renderText(user_text))


if __name__ == "__main__":
    main()
