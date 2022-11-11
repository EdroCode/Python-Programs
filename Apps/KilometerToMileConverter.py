from time import sleep
from tkinter import *


root = Tk()
root.geometry("500x500")
root.title("Mile Converter")

root.mainloop()
while True:

    print("========================")
    print("Metric System Converter")
    print("========================")
    print("")
    
    mile = 0.62137119
        
        
    while True:
            
        initialValue = input("Initial Value (km): ")
        try:
               int(initialValue)
        except ValueError:
            try:
                float(initialValue)
            except ValueError:
                print(f"{initialValue} its not a valid number")
            else:
                finalValue = int(initialValue) * mile
                print(f"[{initialValue}] kilometers are {finalValue} miles :D")
                sleep(1)
                print("")
                print("")
                print("")
                print("")
        else:

            finalValue = int(initialValue) * mile
            print(f"[{initialValue}] kilometers are {finalValue} miles :D")
            sleep(1)
            print("")
            print("")
            print("")
            print("")
        

    
            
            
        