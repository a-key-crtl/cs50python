# Program enables user to place an order, prompting them for items, one per line,
# until user inputs control-d

# Food items w/ corresponding price 
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# User initial ordering price
price = 0

while True:
    try:
        # User selects item off of the menu
        item = input("Item: ").title() #returns string where words start with uppercase character remaining lowercase
        if item in menu:
            price = price + float(menu[item])
            format_price = "{:.2f}".format(price)
            print("Price: $", format_price)
    # When user types ctrl-d on keyboard exits program
    except EOFError:
        print("\n")
        break
    # When user input not found menu dict
    except KeyError:
        pass