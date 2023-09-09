name = input('What is the name of your variable? ')
y = 0
for x in name:
    if x.islower() == True or y == 0:
        print(x.lower(), end="")
        y += 1
    else:
        print("_", x.lower(), sep = "", end="")

print()
