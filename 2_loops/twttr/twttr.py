"""
When texting or tweeting, it's not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.

Implement a program that prompts the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.    
"""


def main():
    user_input = input("Input: ")
    for letter in user_input:
        if letter in "aAeEiIoOuU":
            user_input = user_input.replace(letter, "")
    print(f"Output: {user_input}")


if __name__ == "__main__":
    main()
