names = []
n = 0
while True:
    try:
        names[n] = input("Name: ")
    except EOFError:
        break
    else:
        n += 1

print("Adieu, adieu, to ", end="")
if n == 1:

