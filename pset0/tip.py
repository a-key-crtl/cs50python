def main():
    # Receive input for dollar amount of meal
    dollars = dollars_to_float(input("How much was the meal? "))
    # Receive input for percentage to tip 
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate tip after conversion
    tip = dollars * percent
    # Print how much to leave
    print(f"Leave ${tip:.2f}")

# Function converts dollars string returns as float value 
def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$","")

    return float(d_without_dollar_sign)

# Converts % input to a float value
def percent_to_float(p):
    p_without_percent_sign = p.replace("%","")
    p_converted = float(p_without_percent_sign) / 100
    return p_converted       


main()