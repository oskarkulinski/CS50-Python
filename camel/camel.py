name = input('What is the name of your variable? ')
answer = ""
y = 0
for x in name:
    if x.islower() == True:
        answer[y] = x
        y += 1
    else:
        answer[y] = '_'
        answer[y + 1] = str(x -26)
        y += 2


print (answer)
