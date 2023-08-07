from jar import Jar
import pytest


def test_init():
    # Test initialization with a valid capacity
    jar = Jar(capacity=12)
    assert jar.capacity == 12
    assert jar.size == 0

    # Test initialization with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test initialization with a negative capacity (should raise ValueError)
    try:
        jar = Jar(capacity=-5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12
    # Test deposit more than capacity
    with pytest.raises(ValueError):
        jar.deposit(1)  # 13 is unacceptable


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    # Test withdraw more than available (should raise ValueError)
    with pytest.raises(ValueError):
        jar.withdraw(4)


def test_capacity():
    jar = Jar(capacity=8)
    assert jar.capacity == 8


def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
