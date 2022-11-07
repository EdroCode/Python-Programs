import random
from re import A
import time


soldierNames = ["Jonh", "Robert", "James", "David", "Charles", "Alden", "Gleda", "Annah", "Audrey", "Edward", "Aiken", "Hilda", "Lena"]
bossNames = ["Mapina, knight of dark", "Difera, son of the underworld", "Rafana, hollow lord of blasphomy", "Hell daughter, rarird", "Defiled father, dasoll", "Duman, the frozen", "Refina, warrior of the sky", "Kimon, lord of the forest", "Deprived daughter, eyfana", "Earth prince, lisru", "Joca, The GigaNigga"]

class Soldier:

    def __init__(self, name, age, hp):
        

        
        


        self.name = random.choice(soldierNames)
        self.age = random.randrange(22, 55)
        self.hp = random.randrange(100, 150)


    def TakeDamage(self, damage : int):

        jogador = Soldier(name="", age="" ,hp="")

        print("You take " + str(damage) + " Damage")

        jogador.hp -= damage
        print("Current HP: " + str(self.hp))

        if self.hp <= 0:

            print("You died")

        Decision()
       

      
    

    

    


class Boss:

    def __init__(self, name, hp, damage):
        
      

        self.name = random.choice(bossNames)
        self.hp = random.randrange(200, 300)


    def Attack(self):
        
        damage = random.randrange(20, 35)

    def TakeDamage(self, damage : int):

        boss = Boss(name="", hp="", damage="")
        print("You did " + str(damage) + " Damage")
        boss.hp -= damage
        BossAttack()

  

def Introduction(): 


    print("Welcome To the Arena")
    print("Battle Starting")
    time.sleep(2)
    Battle()
    




def Battle():

    boss = Boss(name="", hp="", damage="")

    print("")
    print("")
    print("")
    print("As soon you walk in to the arena, you see the boss in the distance")
    print("SHOW YOURSELF!!" + "~~" + boss.name)
    print("")
    Decision()
    

  

def Decision():
    print("")
    print("")
    print("")
    print("CHOOSE AN OPTION: 1-ATTACK / 2-HEAL")
    choice = input()
    if choice == "1":
        Attack()
    elif choice == "2":
        pass
    else:
        print("Wrong Input")


def Attack():

    boss = Boss(name="", hp="", damage="")
    dano = random.randrange(20, 35)
    
    boss.TakeDamage(dano)


def BossAttack():
    time.sleep(2)
    print("")
    print("")
    print("")
    print("")
    print("My turn")

    player = Soldier(name="", age="", hp="")
    dano = random.randrange(10, 45)


    player.TakeDamage(dano)



Introduction()



