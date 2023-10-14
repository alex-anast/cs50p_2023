"""
Implement a program that:

- Prompts the user for a level, n. If the user
  does not input a positive integer,
  the program should prompt again.
- Randomly generates an integer between 1 and n,
  inclusive, using the random module.
- Prompts the user to guess that integer.
  If the guess is not a positive integer,
  the program should prompt the user again.
    - If the guess is smaller than that integer,
      the program should output Too small!
      and prompt the user again.
    - If the guess is larger than that integer,
      the program should output Too large!
      and prompt the user again.
    - If the guess is the same as that integer,
      the program should output Just right!
      and exit.
"""


import random


def main():
    level = getLevel("Level: ")
    level = random.randint(1, level)
    while True:
        guess = getLevel("Guess: ")
        if isSame(level, guess):
            break


def getLevel(question="") -> int:
    while True:
        try:
            level = int(input(question))
            if level > 0:
                return level
        except:  # TypeError or ValueError
            pass


def isSame(level: int, guess: int) -> bool:
    if guess < level:
        print("Too small!")
        return False
    elif guess > level:
        print("Too large!")
        return False
    else:
        print("Just right!")
        return True


if __name__ == "__main__":
    main()
