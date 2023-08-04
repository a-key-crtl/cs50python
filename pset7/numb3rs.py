import re



def main():
    print(validate(input("IPV4 Address: ")))
    
    

def validate(ip):
    """Validates ip address inputted by user

    Args:
        ip (string): IPV4 address #.#.#.#

    Returns:
        Boolean: True if IPV4 address is in proper format 
                    where each # is in range [0,255]
                 False if out the range or any other non digit string
    """
    
    # Identify IPV4 address input in #.#.#.# format
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        w = int(matches.group(1))
        x = int(matches.group(2))
        y = int(matches.group(3))
        z = int(matches.group(4))
        
        # Each number must be in the range [0,255] 
        if w >= 0 and w <= 255:
            if x >= 0 and x <= 255:
                if y >= 0 and y <= 255:
                    if z >= 0 and z <= 255:
                        return True
        return False
                    
                
    else:
        return False


if __name__ == "__main__":
    main()