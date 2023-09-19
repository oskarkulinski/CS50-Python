import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    fileName = sys.argv[1].split(".")
    try:
        if fileName[1] != "csv":
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Not a CSV file")
    try:
        fileIn = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Couldn't read " + sys.argv[1])

    fileOut = open(sys.argv[2], "w")
    reader = csv.DictReader(fileIn)
    writer = csv.writer(fileOut)
    writer.writerow(["first", "last", "house"])
    for row in reader:
        fullName = row["name"].split(",")
        writer.writerow([fullName[1].lstrip(), fullName[0], row["house"]])

    fileIn.close()
    fileOut.close()