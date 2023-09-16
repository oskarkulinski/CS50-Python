names = []
n = 0
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
    else:
        n += 1
print()
print("Adieu, adieu, to ", end="")
print(names[0], end = "")
if n > 1:
    for name in names[1:-1]:
        print(",", name, end="")
    print(" and", names[len(names) - 1])


