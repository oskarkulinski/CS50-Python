import jar


def test_jar_general():
    j1 = Jar()
    print(j1)
    print(str(j1.capacity))
    print(str(j1.size))

def test_jar_deposit():
    assert 