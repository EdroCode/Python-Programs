from time import sleep
import random
import math


food = {
    
    "Bread" : 5,
    "Meat" : 30,
    "Sausage" : 20,
    "Pizza" : 30,
    "Fish" : 20


}

total = 0

def MainMenu():

    print("""

    ========================
              MENU
    ========================
    
    1| Buy Itens
    
    
    
    ========================
    
    """)

    awser = input()
    while awser != "1":

        print("Invalid Input")
        awser = input()
    
    if awser == "1":

        BuyMenu()
    
    

def BuyMenu():

    print("""

    ========================
            BUY MENU
    ========================
    
    Avaliable Itens:

    1| Bread
    2| Meat
    3| Sausage
    4| Pizza
    5| Fish
    

    
    ========================
    
    """)

    
    awser = input("Select your products: ")
    
    

    while awser not in ["1", "2", "3", "4", "5"]:
        
        print("Please select a valid product")
        awser = input("Select your products: ")
    
    global total

    if awser == "1":
        total = total + food["Bread"]
    elif awser == "2":
        total = total + food["Meat"]
    elif awser == "3":
        total = total + food["Sausage"]
    elif awser == "4":
        total = total +food["Pizza"]
    elif awser == "5":
        total = total + food["Fish"]
    
    FinalBuy()
    
   

def FinalBuy():

    print("""

    ========================
            CHECKOUT
    ========================
    
    1| Add Discount
    2| Checkout
    
    
    ========================
    
    """)

    choose = input().lower()
    while choose in [1, 2]:

        print("Invalid Input")
        choose = input().lower()
    
    if choose == "1":

        addDiscount()

    if choose == "2":

        Checkout()


def Checkout():

    cash = int(input("Cash "))
    change = cash - total

    while change < 0:

        print("Please give a highter value")
        cash = int(input("Cash "))
        change = cash - total

    

    print("Change = " + str(change))

    awser = input("Go back? (y/n): ")

    while awser not in ["y", "n"]:

        print("Invalid Input")
        awser = input("Go back? (y/n): ")
    
    if awser == "y":

        MainMenu()

    elif awser == "n":

        quit()
    


    


def addDiscount():

    cash = int(input("Cash: "))
    discount = int(input("Discount: ")) / 100
    price_after_discount = total - (discount * total)
    result = price_after_discount
    change = cash - result 

    print("Change = " + str(abs(change)))

    awser = input("Go back? (y/n): ")

    while awser not in ["y", "n"]:

        print("Invalid Input")
        awser = input("Go back? (y/n): ")
    
    if awser == "y":

        MainMenu()

    elif awser == "n":

        quit()
    


MainMenu()
    