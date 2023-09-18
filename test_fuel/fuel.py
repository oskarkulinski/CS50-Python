def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    values = fraction.partition("/")
    #if x or y isn't an integer a ValueError will happen, no need to raise it manually
    x = int(values[0])
    y = int(values[2])
    if y == 0:
         raise ZeroDivisionError
    elif y > x:
         raise ValueError
    else:
        return x * 100 / y


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()