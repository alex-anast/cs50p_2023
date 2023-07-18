'''
Implement a program that prompts the user for a time
and outputs whether it's breakfast time, lunch time, or dinner time.
If it's not time for a meal, don't output anything at all.
Assume that the user's input will be formatted in 24-hour time
as #:## or ##:##. 
And assume that each meal's time range is inclusive.

For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between,
it's time for breakfast.
'''


def main():
    time = input("Give the time: ")
    hours = convert(time)
    print(meal(hours))


def convert(time: str) -> float:
    '''
    assume 24h format
    '''
    time = time.split(':')
    return (float(time[0]) + (float(time[1]) / 60))


def meal(time: float) -> str:
    # breakfast: 7:00 and 8:00
    if 7 <= time <= 8:
        return "breakfast time"
    # lunch: 12:00 and 13:00
    elif 12 <= time <= 13:
        return "lunch time"
    # dinner: 18:00 and 19:00
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return ""


if __name__ == '__main__':
    main()
