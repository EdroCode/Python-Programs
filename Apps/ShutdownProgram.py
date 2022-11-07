from itertools import count
import os
import time

  
  


counting = False
timer : int



print("----SHUTDOWN TIMER----")
print("-----by Edro-----")
print("           ")
print("$$$$$$$_ $$$$$___ $$$$$$__ __$$$___")
print("$$______ $$__$$__ $$___$$_ _$$_$$__")
print("$$$$$___ $$___$$_ $$___$$_ $$___$$_")
print("$$______ $$___$$_ $$$$$$__ $$___$$_")
print("$$______ $$__$$__ $$___$$_ _$$_$$__")
print("$$$$$$$_ $$$$$___ $$___$$_ __$$$___")
print("")
print("")
print("")
print("")
print("")
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")


def countdown():


    counting = True
    timer = int(input("Select Time (s): "))
    
    
    while counting == True:
        
        print(timer)
        timer -= 1
        time.sleep(1)


        if timer == 0:
   
            print("Shutdown")
            os.system("shutdown /s /t 1")
    


    


    









if shutdown == 'no':
    exit()
elif shutdown == "yes":
    

    countdown()



