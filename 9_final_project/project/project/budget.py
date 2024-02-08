# budget.py


"""
"""


from typing import Dict, Union

import auxiliary as aux


def get_user_info() -> Dict[str, Union[int, float]]:
    return {
        'income': get_income(),
        'rent': get_rent(),
        'groceries': get_groceries(),
        'essential_utilities': get_essential_utilities(),
        'income_earning_expenses': get_income_earning_expenses(),
        'healthcare_expenses': get_healthcare_expenses(),
        'minimum_payments_debts_and_loans': get_minimum_payments_debts_and_loans(),
    }


def get_income() -> Union[int, float]:
    receiving_income = aux.get_y_n("Let's start by listing your income. Are you receiving a fixed income? [Y/n] ")
    if not receiving_income:
        pass
    print("Calculate your monthly (equivalent) income.\n")
    print("Apply these two rules:")
    print("    1. If you're paid twice per month, then multiply by two.")
    print("    2. If your monthly income fluctuates, calculate your worst-case or lower-than-average scenario.\n")

    return aux.get_positive_number("Enter your monthly income: ")


def get_rent() -> Union[int, float]:
    print("get_rent function has been called")
    pass


def get_groceries() -> Union[int, float]:
    print("get_groceries function has been called")
    pass


def get_essential_utilities() -> Union[int, float]:
    print("get_essential_utilities function has been called")
    pass


def get_income_earning_expenses() -> Union[int, float]:
    print("get_income_earning_expenses function has been called")
    pass


def get_healthcare_expenses() -> Union[int, float]:
    print("get_healthcare_expenses function has been called")
    pass


def get_minimum_payments_debts_and_loans() -> Union[int, float]:
    print("get_minimum_payments_debts_and_loans function has been called")
    pass


def apply_50_30_20_budget_rule(user_info: Dict[str, Union[int, float]]) -> None:
    """
    50/30/20 Budget Rule
    The 50/30/20 budgeting rule is a simple budgeting strategy to help you prioritize your financial goals:
    50% for Needs: Allocate 50% of your income to cover essential expenses like housing, utilities, groceries, and transportation.
    30% for Wants: Allocate 30% of your income for discretionary spending and non-essential expenses like dining out, entertainment, hobbies, and shopping.
    20% for Savings and Debt Repayment: Allocate 20% of your income towards savings, investments, and paying down debts.
    The purpose of this system is to make sure your essential needs are met, you have room for discretionary expenses, and you prioritize saving for the future and managing your debts.
    These percentages are not set in stone. If money is tight, you may need to allocate a higher percentage of your income to needs. If you have significant debt, you might choose to allocate more than 20% toward debt repayment to accelerate your progress. Similarly, if you have ambitious savings goals, you can allocate a higher percentage to savings.
    """
    pass


def raise_red_flags(user_info: Dict[str, Union[int, float]]) -> None:
    """
    The function should raise red flags based on the user's income and expenses.
    """
    pass