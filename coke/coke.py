x = int('50')
while x > 0:
    coin = int(input('How much did you put in? '))
    if coin == 25 or coin == 10 or coin == 5:
        x = x - coin
    print('Amount due:', x)
    if x <0:
        print('Your change is: ', x)