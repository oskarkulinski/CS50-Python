import sys
import pyfiglet
import random

text = input("Input: ")
if len(sys.argv) == 2:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit()
    try:
        f = pyfiglet.Figlet(font=sys.argv[2])
    except ValueError:
        sys.exit()
elif len(sys.argv) == 0:
    f = pyfiglet.Figlet(font=random.choice(pyfiglet.Figlet().getFonts()))
else:
    sys.exit()

print("Output: ")
print(f.renderText(text))