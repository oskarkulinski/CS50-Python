import sys
import PIL

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    fileName = sys.argv[1].split(".")
    try:
        if fileName[1] != "jpg" or fileName[1] != "jpeg" or fileName[1] != "png":
            sys.exit("Invalid output")
    except IndexError:
        sys.exit("Invalid output")
    else:
        outName = sys.argv[1].split(".")
        if fileName[1] != outName[1]:
            sys.exit("Input and output have different extensions")
    try:
        fileIn = PIL.open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Input does not exist")
