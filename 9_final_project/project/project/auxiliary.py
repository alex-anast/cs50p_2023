# auxiliary.py

"""
Documentation
"""


from typing import Optional, Union


def print_intro() -> None:
    print("\n********************")
    print("  Personal Finance  ")
    print("********************\n")
    print("Welcome to the Personal Finance Calculator!\n")
    print("The goal of this programme is to help you consciously manage your personal finances.\n")
    print("It consists of 7 phases:\n")
    print("    1. Budget and reduce expenses, set realistic goals")
    print("    2. Build an emergency fund")
    print("    3. Employer-sponsored matching funds")
    print("    4. Pay down high interest debts")
    print("    5. Contribute to an IRA")
    print("    6. Save more for retirement")
    print("    7. Save for other goals")
    print("\nLet's get started!\n")


def print_outro():
    print("\nCongratulations! You have completed the Personal Finance Calculator!")
    print("At this point, you should have a clear understanding of budgeting and emergency funds.")
    print("The next steps have not been implemented yet. Get to a good start budgeting and ...")
    print("Stay tuned for updates! Good luck!\n")


def get_y_n(message: Optional[str] = None) -> Optional[str]:
    pass


def get_positive_number(message: Optional[str] = None) -> Optional[Union[int, float]]:
    pass


def get_str(message: Optional[str] = None) -> Optional[str]:
    pass
