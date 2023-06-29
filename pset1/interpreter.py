# Prompting user for an arithmetic expression

expression = input("Enter an expression: ")
x, y, z = expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    print(new_x + new_z)
elif y == "-":
    print(new_x - new_z)
elif y == "*":
    print(new_x * new_z)
else:
    print(new_x / new_z)

