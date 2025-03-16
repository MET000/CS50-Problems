from bank import value


def test_hello():

    assert value("hello") == 0
    assert value("hello, meto") == 0
    assert value("Hello, Mety") == 0


def test_h():

    assert value("hey") == 20
    assert value("hey, meto") == 20
    assert value("Hey, Mety") == 20


def test_other():

    assert value("bonjour") == 100
    assert value("buenos dias, meto") == 100
    assert value("Bonsoir, Mety") == 100
