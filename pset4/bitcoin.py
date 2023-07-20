import sys
import requests
import json

try:
    # If user enters nothing on the command line
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    
    # If user enters more than a float value on command-line
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    # If user input can be converted to float
    elif float(sys.argv[1]):
        try:
            bit_coin_info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = bit_coin_info.json()
            
            # Storing float value of USD rate of bitcoin
            price = o["bpi"]["USD"]["rate_float"]
            
            # Storing user input as n 
            n = float(sys.argv[1])
            
            # Multiplying user input (n) my Bitcoin value for rate
            rate = price * n
            
            # Printing out rate up to four decimal places
            print(f"${rate:,.4f}")
                
        except requests.RequestException:
            sys.exit("There was an ambiguous exception that occurred while handling your request")

# When user does not input a float in command-line
except ValueError:
     sys.exit("Command-line argument is not a number")

