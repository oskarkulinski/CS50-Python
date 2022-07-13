greet = input('What greeting have you received? ')
greet = greet.strip().lower()
if greet == 'hello':
    print('$100')
elif greet.startswith('f')==True:
    print('$20')
else:
    print('$0')