# Program prompts users to input a fruit (case-insensitively) and then outputs the number of 
# calories in one portion of that fruit, per the FDA’s poster for fruits

fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

# Prompts user for item name, loops if not in fruits dict
while True:
    # User inputs item case-insensitively
    item = input("Item: ").lower()
    # User string matches fruits dict, outputs associated calories
    if item in fruits:
        print("Calories:", fruits[item])
        break
