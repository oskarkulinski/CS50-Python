while True:
    frac = input("Fraction: ")
    tup = frac.partition("/")
    try:
        x = int(tup[0])
        y = int(tup[2])
        res = int(x * 100 / y)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
if res >= 99:
    print("F")
elif res <= 1:
    print("E")
else:
    print(f"{res}%")