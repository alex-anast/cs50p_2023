"""
Suppose that you'd like to implement a cookie jar in which to store cookies.
Implement a class called Jar with these methods:

- __init__ should initialize a cookie jar with the given capacity,
  which represents the maximum number of cookies that can fit
  in the cookie jar.  If capacity is not a non-negative int, though,
  __init__ should instead raise a ValueError.
- __str__ should return a str with 🍪, where is n the number of cookies
  in the cookie jar. For instance, if there are 3 cookies in the cookie jar,
  then str should return "🍪🍪🍪"
- deposit should add n cookies to the cookie jar. If adding that many would
  exceed the cookie jar's capacity, though, deposit should
  instead raise a ValueError.
- withdraw should remove n cookies from the cookie jar. Nom nom nom.
  If there aren't that many cookies in the cookie jar, though,
  withdraw should instead raise a ValueError.
- capacity should return the cookie jar's capacity.
- size should return the number of cookies actually in the cookie jar.
"""


class Jar:
    # initialize. Constructor is __new__
    def __init__(self, capacity=12):
        if not capacity >= 0:
            raise ValueError
        # capacity and size are retrieved by the getters
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n

    # decorator: function that modifies the properties
    # of the function below to be strictly getters
    @property  # getter
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(11)
    print(jar)
    print(jar.capacity)
    try:
        jar.capacity = 13
        print(jar.capacity)
    except AttributeError:
        print("capacity cannot be set, all is okay")


if __name__ == "__main__":
    main()
