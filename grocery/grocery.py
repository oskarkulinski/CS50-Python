groceries = {}

while True:
    try:
        item = input()
    except EOFError:
        print()
        groceries = sorted(groceries)
        for thing in groceries:
            print(f"{groceries[thing]} {thing}")
        break
    item = item.upper()
    try:
        groceries[item] += 1
    except KeyError:
        groceries[item] = 1