text = input('What do you want to say? ')
y = len(text) - 1
for x in text:
    if text[x]!='a' or text[x]!='i' or text[x]!='e' or text[x]!='o' or text[x]!='u':
        print(x, end = '')

print('')