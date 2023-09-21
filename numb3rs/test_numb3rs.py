from numb3rs import validate


def main():
    test_validate_correct()
    test_validate_incorrect()


def test_validate_correct():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("194.162.1.17") == True



def test_validate_incorrect():
    assert validate("1.1.1.") == False
    assert validate("256.1.1.1") == False
    assert validate("2.256.1.1") == False
    assert validate("2.4.256.1") == False
    assert validate("2.4.6.256") == False


if __name__ == "__main__":
    main()