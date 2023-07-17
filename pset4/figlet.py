import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    is_random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random_font = False
else:
    print("Invalid usage")
    sys.exit(1)



#Get list of available fonts
figlet.getFonts()

if is_random_font is False:
    try:
        figlet.setFont(font=sys.argv[2])
        
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font = font)
      
msg = input("Input: ")

print("Output: ") 
print(figlet.renderText(msg))
