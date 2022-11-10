from time import sleep
from tkinter import *


window = Tk()

window.geometry("500x600")
window.title("Metric Calculator")

InitialValue = 0
FinalValue = 0




def CentimeterSelecioned():



    pass


















w = Label(window, text='Metric Calculator')
w.grid(row=0, column=1)

Label(window, text='Initial Value').grid(row=3)
Label(window, text='Final Value').grid(row=4)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)


milimeter = IntVar()
Checkbutton(window, text='mm', variable=milimeter).grid(row=3, column=2, sticky=W)
centimeter = IntVar()
Checkbutton(window, text='cm', variable=centimeter, command=CentimeterSelecioned()).grid(row=3, column=3, sticky=W)
deciimeter = IntVar()
Checkbutton(window, text='dm', variable=deciimeter).grid(row=3, column=4, sticky=W)
meter = IntVar()
Checkbutton(window, text='m', variable=meter).grid(row=3, column=5, sticky=W)
kilometer = IntVar()
Checkbutton(window, text='km', variable=kilometer).grid(row=3, column=6, sticky=W)



console = Label(window, text="").grid(row=6)


var2 = IntVar()
Checkbutton(window, text='m', variable=var2).grid(row=4, column=2, sticky=W)




















window.mainloop()



