months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    transformed = date.split("/", 2)
    try:
        day = int(transformed[1])
    except IndexError:
        transformed = date.split(",", 2)
        try:
            day = int(transformed[1])
        except ValueError:
            continue
    except ValueError:
        continue
    else:
        if day > 31:
            continue
    try:
        month = int(transformed[0])
    except ValueError:
        correct = 0
        for m in months:
            if m == transformed[0]:
                correct = 1
                break
    else:
        if month <= 0 or month > 12:
            correct = 0
    if correct == 0:
        continue
    else:
        break

print(f"{transformed[2]}-{transformed[1]}-{transformed[0]}")


