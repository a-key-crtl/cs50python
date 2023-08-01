"""
    Program that expects exactly one command-line argument, 
    the name (or path) of a CSV file in Pinocchio’s format, 
    and outputs a table formatted as ASCII art 
"""

import sys
import csv
from tabulate import tabulate


def main():
    
    check_command_line_arg()
    menu = []
    
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("No such file in directory")
    
    print(tabulate(menu, headers="keys", tablefmt="grid"))
    
    
# Check is file ends in .csv, does not exist, user does not
# specify one command line argument
def check_command_line_arg():   
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
       
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
if __name__ == "__main__":
    main()