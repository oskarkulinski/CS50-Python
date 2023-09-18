from twttr import shorten

def main():
    test_shorten_no_vowels()

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("england") == "nglnd"
    assert shorten("table") == "tbl"


def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("ENGLAND") == "NGLND"
    assert shorten("TABLE") == "TBL"

def test_shorten_no_vowels():
    assert shorten("twttr") == "twttr"
    assert shorten("") == ""
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"


if __name__ == "__main__":
    main()