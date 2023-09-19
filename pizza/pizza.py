import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    fileName = sys.argv[1].split(".")
    try:
        if fileName[1] != "csv":
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")