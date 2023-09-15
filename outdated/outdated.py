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
    try:
        transformed = date.split(",", 2)
    except ValueError:
        transformed = date.split("/", 2)
    try:
        day = int(transformed[1])
    except ValueError:
        pass
    else:
        if day > 31:
            continue
    try:
        month = int(transformed[0])
        
