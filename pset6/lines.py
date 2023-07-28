"""
     Program that expects exactly one command-line argument, 
     the name (or path) of a Python file, and outputs the number of lines of 
     code in that file, excluding comments and blank lines. 
     If the user does not specify exactly one command-line argument, 
     or if the specified file’s name does not end in .py, 
     or if the specified file does not exist, 
     the program should instead exit via sys.exit
"""

import sys

def main():
    # Check the command line arguments
    check_command_line_arg()
    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
      
    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Loop through the lines and check if starts with # or whitespace
    count_lines = 0
    for line in lines:
        if line.isspace() or line.lstrip().startswith('#'):
            pass
        else:
            count_lines += 1
    print(count_lines)            

# Function to check the command line arguments
def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if it is a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    


if __name__ == "__main__":
    main()