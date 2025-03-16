from numb3rs import validate

def test_valid():

    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True

def test_invalid():

    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("2.2.2") == False
    assert validate("100.200") == False
    assert validate("500.100.55.55") == False
    assert validate("1.500.500.500") == False

