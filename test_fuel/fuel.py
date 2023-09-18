def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    values = frac.partition("/")
    try:
        x = int(tup[0])
        y = int(tup[2])
        res = int(round(x * 100 / y, 0))
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if res <= 100:
            break


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()