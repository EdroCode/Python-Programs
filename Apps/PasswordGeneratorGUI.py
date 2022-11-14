import random
from tkinter import *


root = Tk()
root.geometry("300x200")
root.title("Password Generator")



charaters = ["1","2","3","4","5","6","7","8","9","0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "!", "@", "?","#", "$", "*"]




def Randomize():



    print("")
    usr_input = range_input.get()
    print(usr_input)
    user_input = int(usr_input)
    while user_input not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:
        print("")
        password_label.config(text="Please select a valid number between 1 and 50")
        user_input = range_input.get()
            

        

        
    password = random.sample(charaters, user_input)
    password_label.config(f"Your password is: {password}")
        
        
        
    
        

            
title = Label(text="     Password Converter")
title.grid(row=1, column=1)


range_text = Label(text="Select the Range:")
range_text.grid(row=2, column=1)

range_input = Entry()
range_input.grid(row=2, column=2, ipadx=2)

generate_button = Button(text="Generate",command=Randomize)
generate_button.grid(row=3, column=1,columnspan=2, ipadx=80, ipady=1)

password_label = Label(text="Select the range (1-50)" ,borderwidth=1, relief='solid')
password_label.grid(row=4, column=1, columnspan=5, ipadx=48, ipady=40)


                
        

root.mainloop()
