name = input('What is the name of your variable? ')
y = -1
for x in name:
    x = int(x)
    if x.islower() == False:
        y = x+1
    if x == y:
        name[x]  = '_'

print (name)
