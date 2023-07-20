import random


def main():
    level = get_level()
    total_problems = 10
    correct_answers = 0
    while total_problems > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y 
        attempts = 0
        while attempts <= 3:
            try:
                if attempts == 3:
                    print(f"{x} + {y} = {answer}")
                    total_problems = total_problems - 1
                    break
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    total_problems = total_problems - 1
                    correct_answers = correct_answers + 1
                    break
                else:
                        attempts = attempts + 1
                        print("EEE")
                
            except ValueError or KeyError:
                if attempts == 3:
                    print(f"{x} + {y} = {answer}")
                    total_problems = total_problems - 1
                    break
                else:
                    attempts = attempts + 1
                    print("EEE")
    print("Score: ", correct_answers)
                    
                
            
        
    
# Prompts user for a level return 1, 2, or 3
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0 or n > 3:
                pass
            else:
                return n
        except ValueError or TypeError:
            pass
        

# Generates random non-negative integer with level digits or raises ValueError
def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3: 
        return random.randint(100,999)
    else:
        raise ValueError("Only integers 1-3 are allowed!")


if __name__ == "__main__":
    main()