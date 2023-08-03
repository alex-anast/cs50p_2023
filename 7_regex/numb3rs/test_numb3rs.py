from numb3rs import validate


def test_valid_IPv4():
    assert validate("192.168.0.1") is True
    assert validate("10.0.0.1") is True
    assert validate("172.16.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("127.0.0.1") is True
    assert validate("203.0.113.0") is True
    assert validate("198.51.100.0") is True
    assert validate("100.64.0.1") is True
    assert validate("169.254.0.1") is True


def test_invalid_IPv4():
    assert validate("256.0.0.1") is False  # (Octet value exceeds 255)
    assert validate("300.200.100.0") is False  # (Octet value exceeds 255)
    assert validate("192.168.0.0.1") is False  # (Too many octets)
    assert validate("1.2.3.4.5") is False  # (Too many octets)
    assert validate("300.168.1") is False  # (Too few octets)
    assert validate("200.168.1.") is False  # (Too few octets)
    assert validate("192.168.256.1") is False  # (Octet value exceeds 255)
    assert validate("192.168.-1.1") is False  # (Negative value not allowed)
    assert validate("192.168.1.256") is False  # (Octet value exceeds 255)
    assert validate("192.168.01.1") is False  # (Leading zeros not allowed)
