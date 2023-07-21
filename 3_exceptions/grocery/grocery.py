"""
Suppose that you're in the habit of making a list of items
you need from the grocery store.

Implement a program that prompts the user for items,
one per line, until the user inputs control-d
(which is a common way of ending one's input to a program).


Then output the user's grocery list in all uppercase,
sorted alphabetically by item, prefixing each line
with the number of times the user inputted that item.
No need to pluralize the items.
Treat the user's input case-insensitively.
"""


def main():
    grocery_list = {}
    for item in get_items():
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list.update({item: 1})
    print_grocery_list(grocery_list)


def get_items():
    while True:
        try:
            yield input()
        except EOFError:
            break


def print_grocery_list(grocery_list: dict) -> None:
    grocery_list = sort_dict(grocery_list)
    for item in grocery_list:
        print(f"{grocery_list[item]} {item.upper()}")


def sort_dict(A: dict) -> dict:
    return {k: A[k] for k in sorted(A)}


if __name__ == '__main__':
    main()
