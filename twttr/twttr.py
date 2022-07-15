text = input('What do you want to say? ')
x = 0
for x in text:
    if text[x]=='a' or text[x]=='i' or text[x]=='e' or text[x]=='a' or text[x]=='o' or text[x]=='u':
        text[x]= ''
print(text)