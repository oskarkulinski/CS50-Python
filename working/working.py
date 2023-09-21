import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d):?(\d\d)? ([AP]M) to (\d):?(\d\d)? ([AP]M)",s.strip()):
        if int(matches.group(1)) > 12 or int(matches.group(3)) > 12:
            raise ValueError
        elif 
    else:
        raise ValueError


...


if __name__ == "__main__":
    main()