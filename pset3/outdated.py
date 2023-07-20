# Program prompts user for a date in month-day-year order outputs same date in
# YYYY-MM-DD format

# list of months
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Running loop for user input
while True:
    # Prompt user input for date
    date = input("Date: ")

    # Checks if user input start with month name from month list in format Month day, year
    if date.startswith(tuple(month)):

        # Removes comma from string format
        remove_comma_date = date.replace(',', '')

        # Split format into month  day year store in variables 
        x, y, z = remove_comma_date.split(' ')
        v = int(y)

        # Checks if day is >31 
        if v > 31:
            pass
        else:
            m = month.index(x) + 1
            
            print(f"{z}-{m:02}-{v:02}")
            break
    elif date[0].isdigit():
        a, b, c = date.split('/')
        g = int(b)
        f = int(a)
        if g > 31:
            pass
        elif f > 12:
            pass
        else:
            print(f"{c}-{f:02}-{g:02}")
            break
        
