from seasons import difference


def main():
    test_difference()

def test_difference():
    assert difference(["1992" , "02", "13"]) == 46588608000
    assert difference(["1992" , "02", "14"]) == 46588608000
    assert difference(["1992" , "02", "15"]) == 46588608000
    assert difference(["1992" , "02", "16"]) == 46588608000
    assert difference(["1992" , "02", "17"]) == 46588608000