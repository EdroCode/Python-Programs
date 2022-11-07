from random import randrange
from time import sleep



def Game():

    while True:


        
        print("""
        ====================
        Number Guessing Game
        ====================
        """)

        Number = int(input("Choose a number: "))
        range = int(input("Choose a Range: "))
        sleep(.5)
        print("""

        Game is Starting

        """)
        
        sleep(.5)

        guess = randrange(1, range)
        awser = input("Is " + str(guess) + " too High (h), too Low (l), or correct (c) ").lower()   

        

        

            



Game()