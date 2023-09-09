text = input('What do you want to say? ')
for x in text:
    if x =='a' or x=='e' or x == 'i' or x == 'o' or x == 'u' or x=='A' or x=='E' or x=='I' or x == 'O' or x == 'U':
        continue
    else:
        print(x, end = '')

print('')