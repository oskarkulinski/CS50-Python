name = input('What is the name of your variable? ')
for x in name:
    if x.islower() == False:
        name  = '_'

print (name)
