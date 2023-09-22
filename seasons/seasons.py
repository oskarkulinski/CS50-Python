from datetime import date
import re


def main():
    dob = get_date()
    print(difference(dob))



def get_date():
    dob = input("Date of birth: ")
    if matches = re.search(r"(\d{4}-\d{2}-\d{2})", dob):
        return matches.group(1)
    else:
        sys.exit("Invalid Date")

def difference(dob):
    



if __name__ == "__main__":
    main()