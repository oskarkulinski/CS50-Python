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
    if  date.find(",") == -1:
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
            day = int(transformed[1])
        except ValueError:
            continue
        else:
            if day <= 0 or day > 31:
                continue
            else:
                if day < 10:
                    transformed[1] = "0" + transformed[1]
        print(f"{transformed[2].rstrip(' ')}-{transformed[0]}-{transformed[1]}")
        break
    else:
        transformed = date.split(",", 1)
        dm = transformed[0].split(" ", 1)
        try:
            day = int(dm[1])
        except ValueError:
            continue
        else:
            if day <= 0 or day > 31:
                continue
            else:
                if day < 10:
                    dm[1] = "0" + dm[1]
        correct = 0
        for m in months:
            correct += 1
            if m == dm[0].title():
                break
        monthNumber = str(correct)
        if correct < 10:
            monthNumber = "0" + monthNumber

        print(f"{transformed[1].rstrip(' ')}-{monthNumber}-{dm[1]}")
        break

