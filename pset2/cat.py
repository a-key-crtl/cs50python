## while loop
i = 0
while i < 3:
    print("meow")
    i += 1

## for loop
for g in [0, 1, 2]:
    print("woof")

## for loop using range
for d in range(3):
    print("bah")

## use underscore _ to represent variable with no significance
for _ in range(3):
    print("wee")

## print meow three times on new lines
print("meow\n" * 3, end="")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")

main()