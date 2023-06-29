# x = int(input("What's x? "))
# y = int(input("What's y? "))




# print(x + y)


# Calculator to round decimal points
#x = float(input("What's x "))
#y = float(input("What's y "))

#z = x / y

#print(f"{z:.2f}") #specify using f string how many digits you want to print

# print(f"{z:,}") #output will have a comma

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    # or use return pow(n, 2)

main()