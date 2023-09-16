import random


def main():
    ...


def get_level():
    level = 0
    while level != 1 and level != 2 and level != 3:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()