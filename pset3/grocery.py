# Program that prompts the user for items, one per line, 
# until the user inputs control-d then output the user’s grocery list in all uppercase, 
# sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.

# Grocery empty dictionary
grocery = {}

#Loop forever
while True:
    try:
        # Get user input
        item = input().lower()
        # Check if item is already in dictionary
        if item in grocery:
            # If it is, add 1 in the count
            grocery[item] += 1

        # Otherwise, add item for first time
        else:
            grocery[item] = 1    
    except EOFError:
        # Print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        # Stop the while loop
        break
    except KeyError:
        pass