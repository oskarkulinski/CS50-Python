from working import convert
from working import convert_hour


def main():
    test_errors()
    test_nominutes()
    test_minutes()

def test_errors():
    with pytest.raises(ValueError):
        convert(cat)
        


def test_nominutes():


def test_minutes():



if __name__ == "__main__":
    main()