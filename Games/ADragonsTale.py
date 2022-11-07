from cgitb import reset




inputIsWrong = False
caminhoEscolhido = False


print("----A DRAGON TALE----")
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




def Story():
    
    print("Bem vindo a uma nova aventura, qual o teu nome?")
    name = input("Nome: ")
    print("Bem vindo " + name)
    print("Neste mundo de fantasia, heróis como tu lutam diariamente contra monstros para ganhar algum dinheiro")
    print("Pronto para continuar?")
    choice = input("")

    if choice == "S":
        inputIsWrong = False
        print("Bem Vindo a Newground, uma pequena cidade cheia de aventuras")
    elif choice == "N": 
        inputIsWrong = False
        print("Vemo nos em outro código")
    else:
        print("Não percebi, tenta novamente")
        inputIsWrong = True

    
    while inputIsWrong == True:
        choice = input("S ou N: ")
        print("Não percebi, tenta novamente")


    print("")
    print("")
    print("")
    print("")
    print("")
    print("Após um longo dia sem receber dinheiro, finalmente recebeste uma quest importante")
    print("Matar o Rei Goblin da tribo sherklin")
    print("Entusiasmado, segues pela floresta em direção à gruta onde o Rei Goblen vive")
    print("")
    print("Qual caminho escolhes?")
    print("1 - Floresta")
    print("2 - Rio")
    caminho = input()

    while caminhoEscolhido == False:
        caminho = input("")
        print("Não percebi, tenta novamente")



    if caminho == "1":
        pass
    elif caminho == "2":
        pass
    else:
        print("Não percebi, tenta novamente")
        inputIsWrong = True


    
        
        
        


Story()