import random





def RollDice():
    
    while True:   


        print("""
        ===================
          --ROLL A DICE--
        ===================    
              by Edro
            ===========
        """)


        user_input = input("Roll a dice : ")
        rolls = int(user_input.split("d")[0])
        range_value = int(user_input.split("d")[1])
        result = 0
        for x in range(0, rolls):

            temp_result = random.randrange(0, range_value)
            result += temp_result   
            print(temp_result)

        
        print(f"{user_input} = {result}")
            
     

        

RollDice()