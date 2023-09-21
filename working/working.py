import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search(r"(\d):?(\d\d)? ([AP]M) to (\d):?(\d\d)? ([AP]M)",s.strip()):
        if int(hours.group(1)) > 12 or int(hours.group(3)) > 12:
            raise ValueError
        if hours.group(2) != None and hours.group(4) != None:
            if int(hours.group(2)) > 60 or int(hours.group(4)) > 60:
                raise ValueError
            else:
                return
    else:
        raise ValueError


...


if __name__ == "__main__":
    main()