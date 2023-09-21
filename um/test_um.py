from um import count


def main():
    test_count_zero()
    test_count_falsepositives()
    test_count_correct()

def test_count_zero():
    assert count("") == 0
    assert count("blah blah blah") == 0
    assert count("Lorem ipsum dolor sit amet") == 0

def test_count_falsepositives():
    assert count("Yummy") == 0
    assert count("sum") == 0
    assert count("umumumumumumumumum") == 0

def test_count_correct():
    assert count("Regular. um, expressions") == 1
    assert count("Hmmmm um interesting") == 1
    assert count("um") == 1
    assert count("Lorem, um, ipsum, um, dolor, um, sit, um, amet") == 4
    assert count("Lorem, Um, ipsum, um, dolor, Um, sit, UM, amet") == 4



if __name__ == "__main__":
    main()