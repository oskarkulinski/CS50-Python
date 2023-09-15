while True:
        frac = input("Fraction: ")
        x = 
    try:
        x = int(input("Fraction: ")) * 100
    except ValueError:
        pass
    else:
        break
if x >= 99:
    print("F")
elif x <= 1:
    print("E")
else:
    print(x)