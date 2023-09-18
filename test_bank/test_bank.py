from bank import value

def main():
    test_value_lowercase()
    test_value_uppercase()

def test_value_lowercase():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("good morning") == 100
    assert value("hello, sir") == 0

def test_value_uppercase():
    assert value("Hello") == 0
    assert value("Hey") == 20
    assert value("Hood morning") == 100
    assert value("Hello, sir") == 0

def test_value_blank():
    assert value(" hello") == 0
    assert value("  hey") == 20
    assert value("   good morning") == 100
    assert value("    hello, sir") == 0

if __name__ == "__main__":
    main()