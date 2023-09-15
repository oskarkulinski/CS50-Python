groceries = {}

while True:
    try:
        item = input("Item: ")
    except EOFError:
        break
    item = item.upper()
    try:
        total += menu[item]
    except KeyError:
        pass
    else:
        print("Total: ${x:.2f}".format(x = total))
print()