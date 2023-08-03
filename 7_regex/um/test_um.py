from um import count


def test_count_single_um():
    text = "hello, um, world"
    assert count(text) == 1


def test_count_multiple_um():
    text = "um, um, yummy, Um, um, um"
    assert count(text) == 5


def test_count_no_um():
    text = "Hello world!"
    assert count(text) == 0


def test_count_edge_cases():
    text = "um um um um"
    assert count(text) == 4
    text = "um,um,um,um"
    assert count(text) == 4
    text = "um.um.um.um"
    assert count(text) == 4
    text = "yummy, yummy, yummy"
    assert count(text) == 0
