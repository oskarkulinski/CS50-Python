import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.len() < 2 or s.len() > 6:
        return False
    else:
        shortened = s.lstrip(string.ascii_letters)
        if shortened.len() + 2 > s.len():
            return False
        else:
            if shortened.isdigit():
                return True
            else:
                return False


main()