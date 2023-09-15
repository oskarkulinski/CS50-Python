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
    transformed = date.split(",", 2)
    try:
        day = int(transformed[1])
    except ValueError:
        