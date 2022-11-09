import random



def get_response(message):

    p_message = message.lower()

    if p_message == "hello":

        return "Hey :D How did you find me"
    
    if p_message == "roll":

        user_input = input("Roll a dice : ")
        rolls = int(user_input.split("d")[0])
        range_value = int(user_input.split("d")[1])
        result = 0
        for x in range(0, rolls):

            temp_result = random.randrange(0, range_value)
            result += temp_result   
            print(temp_result)

        
        
        return print(f"{user_input} = {result}")
    

    if p_message == "help":

        return """Hey what you need help for?"""

    if p_message == "ping":

        return 
    


    return "Sorry, i didnt understand that :/"