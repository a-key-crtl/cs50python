# Program calculates amount due starting from 50 after user inserts a coin 
# from three denominations: 25 cents, 10 cents, and 5 cents 

# Start setting amount
amount_due = 50
print("Amount Due: ", amount_due)
# Keep running count  of amount due and change owed
while amount_due != 0:

   

    insert_coin = int(input("Insert Coin: "))

    # User inputs 25
    if insert_coin == 25:
       
       # Update amount due with total minus user input
       amount_due = amount_due - insert_coin

       if amount_due == 0:
            print("Change Owed: 0 ")
            break;
       elif amount_due < 0:
            print("Change Owed: ", -amount_due)
            break;     
       else:    
            print("Amount Due: ", amount_due)
            continue
    # User inputs 10
    elif insert_coin == 10:
         # Update amount due with total minus user input
        amount_due = amount_due - insert_coin

        if amount_due == 0:
            print("Change Owed: 0 ")
            break;
        elif amount_due < 0:
            print("Change Owed: ", -amount_due)
            break;     
        else:    
            print("Amount Due: ", amount_due)
            continue
    # User inputs 10
    elif insert_coin == 5:
         # Update amount due with total minus user input
        amount_due = amount_due - insert_coin

        if amount_due == 0:
            print("Change Owed: 0 ")
            break;
        elif amount_due < 0:
            print("Change Owed: ", -amount_due)
            break;     
        else:    
            print("Amount Due: ", amount_due)
            continue
    else:
        print("Amount Due: ", amount_due)
    

 
    