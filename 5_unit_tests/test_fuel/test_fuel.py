import fuel
import pytest


def test_convert():
    with pytest.raises(ValueError):
        fuel.convert("")
        fuel.convert("alex")
        fuel.convert("XXY")
        fuel.convert("a/3")
        fuel.convert("2/1")
        fuel.convert("X/1")
        fuel.convert("2/Y")
        fuel.convert("X/Y")
        fuel.convert("1/2/3")
        fuel.convert("0.5/10")
        fuel.convert("2/-10")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")
    assert fuel.convert("1/2") == 50
    assert fuel.convert("0/1") == 0
    assert fuel.convert("1/1") == 100
    assert fuel.convert("3/4") == 75
    assert fuel.convert("5/8") == 62
    assert fuel.convert("6/9") == 67


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(2) == "2%"
    assert fuel.gauge(10) == "10%"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(90) == "90%"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(100) == "F"
