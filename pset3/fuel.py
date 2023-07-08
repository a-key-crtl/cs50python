# Program prompts user for a fraction formatted as X/Y, wherein each of X and Y is
# and integer, and then outputs as a % rounded to the nearest integer how much fuel
# is in the tank

# Loop will reprompt user each time error occurs
while True:
    try:
        #  Fraction inputed in format integer / integer
        fraction = input("Fraction: ")

        # Splits input to separate numerator and denominator bind to variables
        x, z = fraction.split('/')

        # Reinitialize to numerator and denominator to int data types 
        w, y = int(x), int(z)

        # If numerator is larger than denominator not accepted
        if w > y:
            pass
        # Calculate percent round to nearest int output F if >=99% or E if <=1%
        else:
            percent = round((w/y) * 100)
            if percent >= 99:
                print("F")
                break
            elif percent <= 1:
                print("E")
                break
            else:
                print(f"{percent}%")
                break
    except (ValueError, ZeroDivisionError):
        pass




        