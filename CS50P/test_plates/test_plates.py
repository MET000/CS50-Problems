from plates import is_valid

def test_first_characters():

    assert is_valid("MA") == True
    assert is_valid("zx") == True
    assert is_valid("01") == False
    assert is_valid("M0") == False
    assert is_valid("99") == False


def test_minimum_characters():

    assert is_valid("MAROC") == True
    assert is_valid("REALMADRID") == False
    assert is_valid("a") == False
    assert is_valid("hj") == True


def test_allowed_characters():

    assert is_valid("DA_") == False
    assert is_valid("ar 0") == False
    assert is_valid("aba0") == False
    assert is_valid("$ab") == False
    assert is_valid("AB90") == True

def test_conditions():

    assert is_valid("wq9OO") == False
    assert is_valid("qo0") == False
    assert is_valid("kz55") == True
    assert is_valid("ky50") == True
    assert is_valid("45MO99") == False

