def main():
    # Get time from user
    answer = input("What time is it? ")
    # Call convert function
    time = convert(answer)
    # breakfeast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("Breakfeast Time")
    if time >= 12 and time <= 13:
        print("Lunch Time")
    if time >= 18 and time <= 19:
        print("Dinner Time")

        
def convert(time):
    # get hour and minute
    hours, minutes = time.split(":")
    # Convert time into float number
    new_minute = float(minutes) / 60
    # Return the result to main
    return float(hours) + new_minute

if __name__ == "__main__":
    main()