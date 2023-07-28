from bank import value


def test_case_1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("hElLo") == 0


def test_case_2():
    assert value("h") == 20
    assert value("H") == 20
    assert value("Hfghjk") == 20


def test_case_3():
    assert value("alex") == 100


def test_type():
    assert value("1") == 100


def test_null():
    assert value() == 100


def test_punctuation():
    assert value("Hello, this is a sentence") == 0


def test_spaces():
    assert value(" Hello, this is me") == 0
