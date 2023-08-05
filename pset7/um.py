import re


def main():
    print(count(input("Text: ")))
    
    
# Expects line of text as input as a str and returns as an int number that "um" appears
def count(s):
    um_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_list) 
    
    
    
if __name__ == "__main__":
    main()