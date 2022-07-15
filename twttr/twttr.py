text = input('What do you want to say? ')
y = len(text) - 1
for x in text:
    if x !='a' or x != 'i' or x != 'o' or x != 'u':
        print(x, end = '')

print('')