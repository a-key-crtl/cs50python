

def main():
    # Prompts user for mass as an integer in kilograms
    mass = int(input("Mass (kilograms): "))
    # Prints Energy after passing mass into equation function
    print("E (Joules): ", equation(mass))

# Calculates E = mc^2 returns value
def equation(mass):
    return(mass * pow(300000000,2)) 

main()