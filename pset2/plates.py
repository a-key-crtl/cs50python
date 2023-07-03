# Program prompts user for vanity plate and then output
# Valid if meets all requirements Invalid if it does not

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Checks if user input plate is valid
def is_valid(s):
    # Must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    # Must contain maximum of 6 characters and minimum of 2 characters
    elif len(s) < 2 | len(s) > 6:
        return False
    # Numbers cannot be used in the middle of a plate; they must come at the end
    # first number used cannot be a '0'
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    # No periods, spaces, or punctuation marks allowed
    for d in s:
        if d in ['.', ' ' , '!', '?']:
            return False
    
    # Pass all the tests return true
    return True
    
main()