from plates import is_valid


def test_start_with_two_letters():
    assert is_valid("aa1111") is True
    assert is_valid("1a1111") is False
    assert is_valid("a11111") is False
    assert is_valid("111111") is False
    assert is_valid("11aaaa") is False


def test_min_max():
    assert is_valid("") is False
    assert is_valid("a") is False
    assert is_valid("aa") is True
    assert is_valid("aaa") is True
    assert is_valid("aaaa") is True
    assert is_valid("aaaaa") is True
    assert is_valid("aaaaaa") is True
    assert is_valid("aaaaaaa") is False


def test_num_in_middle():
    assert is_valid("aaaa") is True
    assert is_valid("aaa1") is True
    assert is_valid("aa1a") is False
    assert is_valid("aa11") is True


def test_special_chars():
    assert is_valid("aa.aa") is False
    assert is_valid("aa aa") is False
    assert is_valid("aa!aa") is False
    assert is_valid("aa?aa") is False
    assert is_valid("aa/aa") is False
    assert is_valid("aa_aa") is False


def test_first_num_not_zero():
    assert is_valid("aa01") is False
    assert is_valid("aa10") is True
    assert is_valid("aa101") is True
