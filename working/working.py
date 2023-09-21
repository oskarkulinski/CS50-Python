import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d):?(\d\d)? ([AP]M) to (\d):?(\d\d)? ([AP]M)",s.strip()):
        if
    else:
        raise ValueError


...


if __name__ == "__main__":
    main()