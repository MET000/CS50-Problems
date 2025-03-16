from jar import Jar
import pytest


def test_init():
    jar = Jar()
    with pytest.raises(ValueError):

        jar.__init__(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.__init__(12)

    with pytest.raises(ValueError):

        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.__init__(2)

    with pytest.raises(ValueError):

        jar.deposit(3)
