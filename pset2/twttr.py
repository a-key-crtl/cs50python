# Program prompts the user for a str of text then outputs 
# same text but with all vowels omitted


# Collect user string with vowels
answer = input("Input: ")

# Print "Output: "
print("Output: ", end="")

# Loop through every letter
for letter in answer:
    # Check if it is not vowels whether inputted in upper case or lowercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        # Print the letter
        print(letter, end="")

# Print the new line
print()