from fuel import convert
from fuel import gauge

def main():
    test_conver_valid()
    test_conver_error()
    test_gauge()


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/4") == 50
    assert convert("2/2") == 100
    assert convert("0/3") == 0
    assert convert("1/3") == 33

def test_convert_error():



def test_gauge():



if __name__ == "__main__":
    main()