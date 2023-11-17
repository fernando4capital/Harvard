import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    random_font = False
else:
    sys.exit(1)

figlet.getFonts()

if random_font:
    font = random.choice(figlet.getFonts())
else:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)

sentence = input("Input: ")

print(figlet.renderText(sentence))