import sys
import PIL

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    fileName = sys.argv[2].split(".")
    try:
        if fileName[1].lower() != "jpg" and fileName[1].lower() != "jpeg" and fileName[1].lower() != "png":
            sys.exit("Invalid output")
    except IndexError:
        sys.exit("Invalid output")
    else:
        outName = sys.argv[1].split(".")
        if fileName[1] != outName[1]:
            sys.exit("Input and output have different extensions")
    try:
        photo = PIL.Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    PIL.ImageOps.fit(photo, (100,100))
    shirt = PIL.Image.open("shirt.png")
    shirt.paste(photo)
    shirt.save(sys.argv[2])
    shirt.close()
    photo.close()