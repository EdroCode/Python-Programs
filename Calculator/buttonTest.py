
from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("TEST")


def click():
    
    print("STOP TOUCHING ME")



# BUTTON
button = Button(window,text='START')
button.config(command=click)
button.config(compound='bottom')
button.pack(ipadx= 50, ipady= 50)




def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")


inputtxt = Text(window, height = 10,
    width = 25,
    bg = "light yellow")

Output = Text(window, height = 5,
    width = 25,
    bg = "light cyan")












Output.pack()
inputtxt.pack()
window.mainloop()