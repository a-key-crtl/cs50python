# Program prompts user for names one per line until user inputs 
# control-d then bids adieu
# to those names 

import inflect

p = inflect.engine()

# Create a list to keep track of names
names = []
# Loop forever
while True:
    try:
        # Get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break
# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)