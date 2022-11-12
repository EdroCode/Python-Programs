from time import sleep
from tkinter import *


root = Tk()
root.geometry("300x70")
root.title("Mile Converter")
root.config(background="#bfb1a2")
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




conver_button = Button(root, text="Convert", command=convert, borderwidth=0.5, relief="solid", background="#a56368", fg="#f0ebd8")
conver_button.grid(row=2, column=3)

initial_value = Entry(root, borderwidth=1, relief="solid", fg="#662959")
initial_value.grid(row=2, column=2)

last_value = Label(root, text="", background="#FFFFFF", width=17, borderwidth=0.5, relief="solid", fg="#662959")
last_value.grid(row=2, column=4)


km_label = Label(root, text="Km", borderwidth=0.5, relief="solid", background="#a56368", fg="#f0ebd8")
km_label.grid(row=1,column=2, ipadx=50, ipady=10)

mile_label = Label(root, text="Mile", borderwidth=0.5, relief="solid", background="#a56368", fg="#f0ebd8")
mile_label.grid(row=1,column=4, ipadx=50, ipady=10)





root.mainloop()


            
            
        

        

