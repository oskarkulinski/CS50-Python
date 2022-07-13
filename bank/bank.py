greet = input('What greeting have you received? ')
greet = greet.strip().lower()
if greet.startswith('hello')==True:
    print('$0')
elif greet.startswith('h')==True:
    print('$20')
else:
    print('$100')