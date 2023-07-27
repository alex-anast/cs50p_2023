"""
Little Professor is a “calculator” that generates
ten different math problems for someone to solve.

Implement a program that:

- Prompts the user for a level, n. If the user
  does not input 1, 2, or 3, the program
  should prompt again.
- Randomly generates ten (10) math problems
  formatted as X + Y = , wherein each of X and Y
  is a non-negative integer with n digits.
  No need to support operations other than addition (+).
- Prompts the user to solve each of those problems.
  If an answer is not correct (or not even a number),
  the program should output EEE and prompt the user again,
  allowing the user up to three tries in total for that problem.
  If the user has still not answered correctly after three tries,
  the program should output the correct answer.
- The program should ultimately output the user's score:
  the number of correct answers out of 10.
"""


from random import randint
from sys import exit


def main():
    level = get_level("Level: ")
    score = 0
    count_wrong = 0
    for i in range(10):
        if count_wrong == 0:  # else re-ask
            x = generate_integer(level)
            y = generate_integer(level)
        # user can answer 3 times before losing point
        for j in range(3):
            answer = input(f"{x} + {y} = ")
            try:
                if int(answer) == x + y:
                    count_wrong = 0
                    score += 1
                    break
                else:
                    # jump to error handling
                    raise ValueError
            except:
                # if mistake is the third one
                if count_wrong == 2:
                    count_wrong = 0
                    # give the answer
                    print(f"{x} + {y} = {x + y}")
                # else, keep counting
                else:
                    count_wrong += 1
                    print("EEE")
    print(f"Score: {score}")


def get_level(string_req: str = ""):
    while True:
        try:
            level = int(input(string_req))
            if level in [1, 2, 3]:
                return level
        except:
            # just re-prompt
            pass


# non negative integer with n digits
def generate_integer(level) -> int:
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)
    else:
        exit("Level should be 1, 2 or 3")


if __name__ == "__main__":
    main()
