import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = len(re.findall(r"(?:^|[^\w])(um)(?:[^\w]|$)", s, re.IGNORECASE))
    return count



if __name__ == "__main__":
    main()