def main():
    while True:
        try:
            #  Fraction inputed in format integer / integer
            fraction = input("Fraction: ")
            print(convert(fraction))
            break
        except (ValueError, ZeroDivisionError):
            print("Error")


def convert(fraction):
    try:
        # Splits input to separate numerator and denominator bind to variables
        x, z = fraction.split('/')

        # Reinitialize to numerator and denominator to int data types 
        w, y = int(x), int(z)
        if w > y:
            return "Error"
        percentage = round((w/y) * 100)   
        return gauge(percentage)
    except ValueError or ZeroDivisionError:
            return "Error"


def gauge(percentage):
            if percentage >= 99:
                return "F"
            elif percentage <= 1:
                return "E"
            else:
                return f"{percentage}"


if __name__ == "__main__":
    main()