from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert_valid()
    test_convert_error()
    test_gauge()


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/4") == 50
    assert convert("2/2") == 100
    assert convert("0/3") == 0
    assert convert("1/3") == 33

def test_convert_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()