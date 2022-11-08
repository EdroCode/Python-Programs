import random





def RollDice():

    print("""
    
    =================== 
    -----ROLL DICE-----
    ===================
    
    """)


    times = input("How many times you want to roll? (ex:1)")
    diceNumber = input("What value you want to roll) (ex:6)")
    

    while times not in [1,2,3,4,5,6,7,8,9,0,"d"]:

        print("Thats not a Dice")
        print("You should input the dice like this (1d20)")
        times = input("How many times you want to roll? (ex:1)")
        
    while diceNumber not in [1,2,3,4,5,6,7,8,9,0,"d"]:

        print("Thats not a Dice")
        print("You should input the dice like this (1d20)")
        diceNumber = input("What value you want to roll) (ex:6)")
            
    dice = random.randrange(diceNumber, diceNumber)


    pass



RollDice()