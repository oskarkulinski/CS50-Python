from plates import is_valid

def main():
    test_is_valid_short()
    test_is_valid_long()

def test_is_valid_short():
    assert is_valid("aa") == False
    assert is_valid("AA") == False
    assert is_valid("AAaaAA") == True
    assert is_valid("aAAa") == True

def test_is_valid_long():
    assert is_valid("aaaaaaa") == False
    assert is_valid("AaaaaaA") == False
    assert is_valid("aaaaaa") == True

def test_is_valid_letters():
    assert is_valid("aa1111") == True

    assert is_valid("a1111") == False
    assert is_valid("11") == False
    assert is_valid("aaa1") == True
    assert is_valid("aa1a1") == False
    assert is_valid("aa,11") == False

def test_is_valid_numbers():
    assert is_valid("aa111a") == False


if __name__ == "__main__":
    main()