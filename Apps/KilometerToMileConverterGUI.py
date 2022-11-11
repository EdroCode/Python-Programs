from time import sleep
from tkinter import *


root = Tk()
root.geometry("300x50")
root.title("Mile Converter")

mile = 0.62137119




def convert():


    global warning_text
    warning_text = "not a valid number"


    global final_text
    final_text = ""


    global first_value    
    first_value = initial_value.get()
    try:
        int(first_value)
    except ValueError:
        try:
            float(first_value)
        except ValueError:
            last_value.config(text=warning_text)
        else:
            finalValue = int(first_value) * mile
            last_value.config(text=finalValue)
            
                    
                
    else:
        finalValue = int(first_value) * mile
        last_value.config(text=finalValue)




conver_button = Button(root, text="Convert", command=convert)
conver_button.grid(row=2, column=3)

initial_value = Entry(root)
initial_value.grid(row=2, column=2)

last_value = Label(root, text="", background="#FFFFFF", width=20)
last_value.grid(row=2, column=4)


km_label = Label(root, text="Km")
km_label.grid(row=1,column=2)

mile_label = Label(root, text="Mile")
mile_label.grid(row=1,column=4)





root.mainloop()


            
            
        

        

