from um import count


def test_count_1():

    assert count("um") == 1
    assert count("Hello, um, yo") == 1
    assert count("um, yum") == 1
    assert count("Um") == 1


def test_count_0():

    assert count("umy") == 0
    assert count("yum") == 0
    assert count("Hey, umy") == 0


def test_count_n():

    assert count("um, um, um") == 3
    assert count("Hey, um, um hany") == 2
    assert count("um,um,um,um,um") == 5
