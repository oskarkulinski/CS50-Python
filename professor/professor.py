import random


def main():
    n = get_level()
    correct = 0
    for i in range(0,10):
        x = generate_integer(n)
        y = generate_integer(n)
        answer = x + y
        for _ in range(0, 3):
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            else:
                if guess == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
    print("Score:", correct)

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
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)
    else:
        raise ValueError
    return integer

if __name__ == "__main__":
    main()