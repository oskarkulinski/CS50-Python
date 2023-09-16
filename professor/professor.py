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
    return level


def generate_integer(level):
    if level == 1:
        integer = random.randomint(1, 9)
    elif level == 2:
        integer = random.randomint(10, 99)

if __name__ == "__main__":
    main()