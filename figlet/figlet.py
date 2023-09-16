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
else:
    f = pyfiglet.Figlet(font=random.choice(pyfiglet.Figlet().getFonts()))

print("Output: ")
print(f.renderText(text))