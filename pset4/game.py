'''
    Program prompts user fo a level, n then randomly generates and int
    between 1 and n, inclusive randomly. Prompts user to guess integer
    with hints to correctly guess such as too large/small
'''

import random 

# Repeatedly prompt user to input level integer n > 1
while True:
    try:
        # User inputs level n 
        level = int(input("Level: "))
        
        # Negative integers are not accepted
        if level < 1:
            pass
        else:
            # Generating random integer between 1 and user input integer
            answer = random.randint(1,level)
            
            # Running loop for the user's guess until correct
            while True:
                try:
                    guess = int(input("Guess: "))
                    
                    # If guess is smaller than answer
                    if guess < answer:
                        print("Too small!")
                    
                    # If guess is larger than the answer
                    elif guess > answer:
                        print("Too large!")
                    # If user guesses correctly
                    else:
                        print("Just right!")
                        break
                except ValueError or TypeError:
                    pass
        break      
    except ValueError or TypeError:
        pass
