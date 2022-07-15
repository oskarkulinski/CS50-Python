text = input('What do you want to say? ')
y = len(text) - 1
x = 0
while x <= y:
    if text[x]=='a' or text[x]=='i' or text[x]!='e' or text[x]!='o' or text[x]!='u':
        print(text[x], end = '')
    else:
        print('')

    x= x + 1
print('')