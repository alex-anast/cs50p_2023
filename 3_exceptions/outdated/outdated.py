"""
In the United States, dates are typically
formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is
arguably bad design.
Dates in that format can't be easily sorted because
the date's year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000
chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous.
Harvard was founded on September 8, 1636, but 9/8/1636
could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601,
an international standard that prescribes
that dates should be formatted in year-month-day
(YYYY-MM-DD) order, no matter the country,
formatting years with four digits, months with two digits,
and days with two digits, “padding” each with leading zeroes.

Implement a program that prompts the user for a date,
anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636.

Then output that same date in YYYY-MM-DD format.
If the user's input is not a valid date in either format,
prompt the user again. Assume that every month has no more than
31 days; no need to validate whether a month
has 28, 29, 30, or 31 days.
"""


from enum import Enum


class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


def main():
    print(date_today())


def date_today() -> str:
    while True:
        date = input("Date: ")
        try:
            # 9/8/1636
            if "/" in date:
                date = date.split("/")
                day = int(date[1])
                month = int(date[0])
                year = int(date[2])
                if day <= 31 and month <= 12:
                    break
            # September 8, 1636
            elif " " in date:
                date = date.split(" ")
                try:
                    date[0] = Month[date[0]].value
                except ValueError as err:
                    print(f"ValueError: {err}")
                # testing forces me to assume comma
                # ... will always be there:
                day = int(date[1][:-1])
                month = int(date[0])
                year = int(date[2])
                if day <= 31 and month <= 12:
                    break
        # re-prompt
        except KeyError:
            continue
        except ValueError:
            continue
    return f"{year}-{month:02d}-{day:02d}"


if __name__ == "__main__":
    main()
