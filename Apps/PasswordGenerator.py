import random


charaters = ["1","2","3","4","5","6","7","8","9","0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "!", "@", "?","#", "$", "*"]




def Randomize():


    while True:

        print("")
        user_input = input("Select the password range (1-50): ")
        user_input = int(user_input)
        while user_input not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:
            print("")
            print("Please select a valid number between 1 and 50")
            user_input = input("Select the password range (1-50): ")
            

        

        
        password = random.sample(charaters, user_input)
        print("")
        print("Your password is: ", end="")
        for x in password:


            result = print(x, end="")
        
        
    
        

            
        


               
                
        



Randomize()
