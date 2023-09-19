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
    writer = csv.DictWriter(fileOut, ["first", "last", "house"])
    for row in reader:
        try:
            fullName = row[0].split(",")
        except KeyError:
            continue
        else:
            writer.writerow([fullName[0], fullName[1], row[1]])

    fileIn.close()
    fileOut.close()