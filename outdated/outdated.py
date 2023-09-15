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
    if  date.lfind(",") == -1:
        transformed = date.split("/", 2)
        try:
            month = int(transformed[0])
        except ValueError:
            continue
        else:
            if month <= 0 or month > 12:
                continue
            else:
                if month < 10:
                    transformed[0] = "0" + transformed[0]
        try:
            day = int(transfomred[1])
        except ValueError:
            continue
        else:
            if day <= 0 or day > 31:
                continue
            else:
                if day < 10:
                    transformed[1] = "0" + transformed[1]
    else
        transformed = date.split(",", 1)
        dm = transformed[0].split(" ", 1)
        try





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
    correct = 1
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

print(f"{transformed[2]}-{transformed[0]}-{transformed[1]}")


