# Ask user for their name
name = input("What's your name?")

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Split user's name into first name and last name
# first, last = name.split(" ")
# or you can name = input("Whats your name? ").strip().title() to clean up your code #

# Say hello to user
# print(f"hello, {first}")

# Ask user for their name
# name = input("What's your name? ").strip().title()

# Say hello to user
# print(f"hello, {name}")


# Everything indented under this def is meaning on hello() func
# def hello():
 #   print("hello")

# name = input("What's your name? ")
# hello(name) #passing name to hello(to) def

def main():
    hello()
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main() #calls main() which calls hello()