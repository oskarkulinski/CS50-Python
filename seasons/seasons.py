from datetime import date
import re
import sys

def main():
    dob = get_date()
    print(difference(dob))



def get_date():
    dob = input("Date of birth: ")
    if matches := re.search(r"(\d{4})-(\d{2})-(\d{2})", dob):
        return matches.groups()
    else:
        sys.exit("Invalid Date")

def difference(dob):
    birthdate = date(int(dob[0]), int(dob[1]), int(dob[2]))
    currentDate = date.today()
    difference = currentDate - birthdate
    print(difference)



if __name__ == "__main__":
    main()