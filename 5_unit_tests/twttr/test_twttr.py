from twttr import shorten


def test_nullEntry():
    assert shorten("") == ""


def test_lowercase():
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("HELLO") == "HLL"


def test_title():
    assert shorten("Hello") == "Hll"


def test_typeError():
    assert shorten("1") == "1"
    assert shorten("[1]") == "[1]"


def test_punctuation():
    assert shorten("Hello, this is a world.!") == "Hll, ths s  wrld.!"
