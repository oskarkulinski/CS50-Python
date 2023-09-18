from plates import is_valid

def main():
    test_is_valid_short()
    test_is_valid_long()

def test_is_valid_short()
    assert is_valid("aa") == False
    assert is_valid("AA") == False
    assert is_valid("AAaaAA") == True
    assert is_valid("aAAa") == True

def test_is_valid_long()
    assert is_valid("aaaaaaa")
    assert is_valid("AaaaaaA")

def test_is_valid_letters()


def test_is_valid_numbers()