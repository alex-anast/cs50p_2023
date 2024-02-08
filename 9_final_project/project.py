# project.py

import logging

import auxiliary as aux
import budget
import emergency_fund


logger = logging.Logger(__name__)


def main():
    logger.debug("Starting execution")
    aux.print_intro()

    calculate_budget()
    logger.info("Budget calculated")

    calculate_emergency_fund()
    logger.info("Emergency fund built")

    aux.print_outro()
    logger.info("Execution finished")

    if ask_save_results() is True:
        export_to_csv()
        logger.info("Results saved to CSV file")


def calculate_budget():
    """
    https://www.reddit.com/r/personalfinance/wiki/budgeting/
    """
    user_info = budget.get_user_info()
    budget.apply_50_30_20_budget_rule(user_info)
    budget.raise_red_flags(user_info)


def calculate_emergency_fund():
    """
    https://www.wisebread.com/figuring-the-size-of-your-emergency-fund
    """
    pass


def ask_save_results() -> bool:
    if aux.get_y_n("Would you like to save the results to a CSV file? (y/n): "):
        logger.debug("Saving the results to a CSV file ...")
        pass
    else:
        logger.debug("User chose not to save the results to a CSV file")
        return


def export_to_csv():
    pass


if __name__ == "__main__":
    main()
