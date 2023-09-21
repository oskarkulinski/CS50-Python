from working import convert
from working import convert_hour
import pytest


def main():
    test_errors()
    test_nominutes()
    test_minutes()

def test_errors():
    with pytest.raises(ValueError):
        convert("cat")
        convert("9 am 5 pm")
        convert("19 AM to 5 PM")
        convert("9 AM to 15 PM")
        convert("9:60 AM to 5:40 PM")
        convert("9:59 AM to 5:75 PM")



def test_nominutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"
    assert convert("6 PM to 11 PM") == "18:00 to 23:00"

def test_minutes():
    assert convert("9:51 AM to 5:42 PM") == "09:51 to 17:42"
    assert convert("9:16 PM to 5:16 AM") == "21:16 to 05:16"
    assert convert("9:59 AM to 10:00 AM") == "09:59 to 10:00"
    assert convert("6:33 PM to 11:30 PM") == "18:33 to 23:30"


if __name__ == "__main__":
    main()