name = input('What is the name of your variable? ')
answer = ""
for x in name:
    if x.islower() == True:
        print(x, end="")
    else:
        print("_", x.lower, end="")

print()
