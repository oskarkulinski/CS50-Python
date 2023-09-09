import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        shortened = s.lstrip(string.ascii_letters)
        if len(shortened) + 2 > len(s):
            return False
        else:
            if shortened != None and shortened.isdigit() and shortened[0] != '0':
                return True
            else:
                return False


main()