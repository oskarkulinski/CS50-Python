from jar import Jar
import pytest

def test_jar_general():
    j1 = Jar()
    assert print(j1) == ""
    assert print(str(j1.capacity)) == "12"
    assert print(str(j1.size)) == "0"

def test_jar_deposit():
    j1 = Jar()
    j1.deposit(10)
    assert print(j1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert print(str(j1.capacity)) == "12"
    assert print(str(j1.size)) == "10"
    with pytest.raises(ValueError):
        j1.deposit(5)

def test_jar_withdraw():
    j1 = Jar()
    j1.deposit(10)
    j1.withdraw(5)
    assert print(j1) == "🍪🍪🍪🍪🍪"
    assert print(str(j1.capacity)) == "12"
    assert print(str(j1.size)) == "5"
    with pytest.raises(ValueError):
        j1.withdraw(10)


def test_jar_other():
    j1 = Jar()
    j1.deposit(10)
    j1.withdraw(5)
    assert print(j1) == "🍪🍪🍪🍪🍪"
    assert print(str(j1.capacity)) == "12"
    assert print(str(j1.size)) == "5"

    j1.size = 9
    j1.capacity = 10

    assert print(j1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert print(str(j1.capacity)) == "10"
    assert print(str(j1.size)) == "9"
    with pytest.raises(ValueError):
        j1.withdraw(10)
        j1.deposit(5)