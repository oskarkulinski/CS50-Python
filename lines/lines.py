import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    fileName = sys.argv[1].split(".")
    try:
        if fileName[1] != "py":
            sys.exit("Not a Python file")
    except IndexError:
        sys.exit("Not a Python file")
    counter = 0
    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.lstrip().startswith("#") == False and line.isspace() == False:
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(counter)