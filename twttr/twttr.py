text = input('What do you want to say? ')
x = len(text) - 1

while x >0:
    if text[x]=='a' or text[x]=='i' or text[x]=='e' or text[x]=='a' or text[x]=='o' or text[x]=='u':
        text[x]= ''
    x= x -1
print(text)