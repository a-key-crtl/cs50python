# Program prompts the user for a str of text then outputs 
# same text but with all vowels omitted


# Collect user string with vowels
vowel = input("Input: ")

for v in vowel:
    print("Output: ")
    match v:
        case "a" | "A" | "e" | "E" | "i" | "I" | "O" | "o" | "u" | "U":
            print(v.replace(""))
        case _:
            print(v)

