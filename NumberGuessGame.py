from time import sleep
import random





def Game():


    while True:



        print("""
        ====================
        Number Guessing Game
        ====================
        """)

        range = int(input("Select The Range: "))
        print("""
        Game is Starting
        """)
        number = random.randrange(0,range)
        sleep(1)
        x = int(input("Guess the Number: "))
        if x > number:
            print("Lower")
        elif x < number:
            print("Higher")

        while x != number:

            x = int(input("Guess the Number: "))

            if x > number:
                print("Lower")
            elif x < number:
                print("Higher")
            elif x == number:
                awser = input("You win, restart (y/n)? ").lower()
                
                if awser == "y":
                    break
                elif awser == "n":
                    quit()
                



Game()