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
        s.lstrip()


main()