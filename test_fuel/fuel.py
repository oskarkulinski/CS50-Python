def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    values = frac.partition("/")
    try:
        x = int(tup[0])
        y = int(tup[2])
    except ValueError:
        raise ValueError
    else:
        if y == 0:
            raise ZeroDivisionError
        elif y > x:
            raise ValueError


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()