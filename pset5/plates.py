def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Must contain maximum of 6 characters and minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False
    # Must start with at least two letters
    elif s[0].isalpha() is False or s[1].isalpha() is False:
        return False
    # Numbers cannot be used in the middle of a plate; they must come at the end
    # first number used cannot be a '0'
    i = 0
    while i < len(s):
        if s[i].isalpha() is False:
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
    


if __name__ == "__main__":
    main()