groceries = {}

while True:
    try:
        item = input("Item: ")
    except EOFError:
        for thing in groceries
            print(f"{groceries[thing]} {thing}")
        break
    item = item.upper()
    try:
        total += menu[item]
    except KeyError:
        groceries[item] = 0
print()