from seasons import difference


def main():
    test_difference()

def test_difference():
    assert difference(["1999" , "02", "13"]) == 12941280
    assert difference(["1999" , "02", "14"]) == 12939840
    assert difference(["1999" , "02", "15"]) == 12938400
    assert difference(["2023" , "09", "21"]) == 1440
    assert difference(["1992" , "11", "17"]) == 16223040

if __name__ == "__main__":
    main()