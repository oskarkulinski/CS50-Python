math = input('What do you want to calculate? ')

math = math.strip()
x, y, z = math.split()

x = float(x)
z = float(z)

match y:
    case '+':
        result = x + z
    case '-':
        result = x - z
    case '*':
        result = x*z
    case '/':
        result = x/z