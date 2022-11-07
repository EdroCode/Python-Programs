


morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}






def encrypt(phrase):
    
    cipher = ''
    for letter in phrase:
        
        if letter != ' ':
 
            cipher += morse_code[letter] + ' '
        else:
           
            cipher += ' '
 
    return cipher

def Decrypt(message):
    
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 

        if (letter != ' '):
 
            i = 0
 
            citext += letter
 
        else:

            i += 1
 
            if i == 2 :

                decipher += ' '

            else:
                
                decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
                citext = ''

 
    return decipher

def main():
    
    print("""
    
    ===================
       --MORSE CODE--
        -TRANSLATOR- 
    ===================
    
    
    """)
    awser = input(
        
        """What you want to do?
        --------------------------------
        1| Encrypt
        2| Decrypt
        3| Check Morse Code Dictionary
        --------------------------------

    """)

    if awser == "1":

        print("")
        message = input("Enter your phrase: ")
        result = encrypt(message.upper())
        print (result)

    elif awser == "2":
        
        print("")
        message = input("Enter your phrase: ")
        result = Decrypt(message)
        print(result)



    while awser != "1" or "2" or "3":

        print("Wrong Input")
        
        awser = input(
        
        """What you want to do?
        --------------------------------
        1| Encrypt
        2| Decrypt
        --------------------------------

        """)
        


        if awser == "1":
            
            print("")
            message = input("Enter your phrase: ")
            result = encrypt(message.upper())
            print (result)

        elif awser == "2":
            
            print("")
            message = input("Enter your phrase: ")
            result = Decrypt(message)
            print(result)


        



    

    
 
    

main()