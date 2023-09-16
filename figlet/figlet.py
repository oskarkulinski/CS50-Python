import sys
import pyfiglet
import random

if len(sys.argv) == 2:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Wrong first argument")
    try:
        f = pyfiglet.Figlet(font=sys.argv[2])
    except ValueError:
        sys.exit("This font does not exist")
elif len(sys.argv) == 0:
    f = pyfiglet.Figlet(font=random.choice(pyfiglet.Figlet().getFonts()))
else:
    sys.exit("Wrong amount of arguments")

text = input("Input: ")
print("Output: ")
print(f.renderText(text))