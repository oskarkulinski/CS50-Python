name = input('What is the name of your variable? ')
for x in name:
    if x.islower() == False:
        name[x+1]  = '_'

print (name)
