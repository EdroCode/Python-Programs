  
from dbm import ndbm
from lib2to3.pgen2.token import NEWLINE



print("----MATH CALCULATOR----")
print("-----by Edro-----")
print("           ")
print("$$$$$$$_ $$$$$___ $$$$$$__ __$$$___")
print("$$______ $$__$$__ $$___$$_ _$$_$$__")
print("$$$$$___ $$___$$_ $$___$$_ $$___$$_")
print("$$______ $$___$$_ $$$$$$__ $$___$$_")
print("$$______ $$__$$__ $$___$$_ _$$_$$__")
print("$$$$$$$_ $$$$$___ $$___$$_ __$$$___")
print("")


def start():
    
    print("Selecione o Modo de Calculadora: ")
    print("1| ÁREAS")
    print("2| VOLUMES")
    print("3| PERIMETROS")
    print("4| FQ")
    print("5| OUTROS")
    print("           ")
    mode = input("Modo: ")

    if mode == "1":

        AreaMode()
    elif mode == "2":

        VolumeMode()
    elif mode == "3":

        PerimetrosMode()
    else:

        print("Esse modo não existe")
        



#=================================
#             MODOS
#=================================


def AreaMode():

    print("           ")
    print("           ")
    print("Modo Selecionado")
    print("           ")
    print("Seleciona a Area que queres calcular:")
    print("           ")
    print("1| Circunferência")
    print("2| Quadrado/Retângulo")
    print("3| Triângulo")
    print("4| Trapézio")
    print("5| Losângulo")
    print("6| Cubo")
    print("7| Cilindro")
    print("8| Cone")
    print("9| Esfera")
    print("           ")
    
    areaSelected = input("Modo: ")


    if areaSelected == "1":

        # Circunferência
        print("")
        print("")
        print("Circunferência")
        print("")
        print("")
        raio = int(input("Raio: "))
        PI = 3.142
        result = PI * (raio * raio)
        print("Área: " + str(result))

    
    elif areaSelected == "2":

        print("-------")
        print("")
        # Quadrado/Retângulo
        print("")
        print("")
        print("Quadrado/Retãngulo")
        print("")
        print("")
        largura = int(input("Largura: "))
        altura = int(input("Altura: "))
        result = largura * altura
        print("Área: " + str(result))
    

    elif areaSelected == "3":

        print("-------")
        print("")
        # Triângulo
        print("Triângulo")
        print("")
        print("")
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        result = (base * altura) / 3
        print("Área: " + str(result))


    elif areaSelected == "4":
        
        print("-------")
        print("")
        # Trapézio
        print("Trapézio")
        print("")
        print("")
        baseMaior = int(input("Base Maior: "))
        baseMenor = int(input("Base Menor: "))
        altura = int(input("Altura: "))
        result = ( (baseMaior + baseMenor) / 2 ) * altura
        print("Área: " + str(result))


    elif areaSelected == "5":
        
        print("-------")
        print("")
        # Losângulo
        print("Losângulo")
        print("")
        print("")
        baseMaior = int(input("Diagonal Maior: "))
        baseMenor = int(input("Diagonal Menor: "))
        result = (baseMaior * baseMenor) / 2 
        print("Área: " + str(result))


    elif areaSelected == "6":
         
        print("-------")
        print("")
        # Cubo
        print("Cubo ( ÁREA TOTAL) ")
        print("")
        print("")
        aresta = int(input("Aresta: "))
        result = aresta * 6
        print("Área Total: " + str(result))


    elif areaSelected == "7":
        
        print("-------")
        print("")
        # Cilindro
        print("Cilindro")
        print("")
        print("")
        raio = int(input("Raio: "))
        altura = int(input("Altura: "))
        PI = 3.142
        resultLateral = 2 * PI * raio * altura
        resultBase = PI * (raio * raio)
        resultTotal = (2 * resultBase) + resultLateral
        print("Área Total: " + str(resultTotal))
        print("Área Lateral: " + str(resultLateral))
        print("Área da Base: " + str(resultBase) )


    elif areaSelected == "8":
            
        print("-------")
        print("")
        # Cone
        print("Cone")
        print("")
        print("")
        raio = int(input("Raio: "))
        altura = int(input("Altura: "))
        PI = 3.142
        geratriz = ((altura * altura) + (raio * raio)) ** (1/2)
        resultLateral = PI * raio * geratriz
        resultBase = PI * (raio * raio)
        resultTotal = PI * raio * (geratriz + raio)
        print("Geratriz: " + str(geratriz))
        print("Área Total: " + str(resultTotal))
        print("Área Lateral: " + str(resultLateral))
        print("Área da Base: " + str(resultBase) )


    elif areaSelected == "9":
        
        print("-------")
        print("")
        # Esfera
        print("Esfera")
        print("")
        print("")
        raio = int(input("Raio: "))
        PI = 3.142
        result = 4 * PI * (raio * raio)
        resultPi = 4 * (raio * raio)
        print("Área Total: " + str(result))
        
    
    else:

        print("Wrong Mode")

def VolumeMode():
    
    print("           ")
    print("           ")
    print("Modo Selecionado")
    print("           ")
    print("Seleciona o Volume que queres calcular:")
    print("           ")
    print("1| Cubo")
    print("2| Paralelepípedo")
    print("3| Cilindro")
    print("4| Cone")
    print("5| Esfera")
    print("           ")
    
    areaSelected = input("Modo: ")


    if areaSelected == "1":
        
        # Cubo
        print("")
        print("")
        print("Cubo")
        print("")
        print("")
        aresta = int(input("Aresta: "))
        result = (aresta * aresta * aresta)
        print("Volume: " + str(result))
    
    
    elif areaSelected == "2":
        
        # Paralelepípedo
        print("")
        print("")
        print("Paralelepípedo")
        print("")
        print("")
        comprimento = int(input("Comprimento: "))
        largura = int(input("Largura: "))
        altura = int(input("Altura: "))
        result = (comprimento * largura * altura)
        print("Volume: " + str(result))


    elif areaSelected == "3":
        
        # Cilindro
        print("")
        print("")
        print("Cilindro")
        print("")
        print("")
        raio = int(input("Raio: "))
        altura = int(input("Altura: "))
        PI = 3.142
        result = (PI * (raio * raio) * altura)
        print("Volume: " + str(result))


    elif areaSelected == "4":
        
        # Cone
        print("")
        print("")
        print("Cone")
        print("")
        print("")
        raio = int(input("Raio: "))
        altura = int(input("Altura: "))
        PI = 3.142
        result = ((PI * (raio * raio) * altura) / 3)
        print("Volume: " + str(result))


    elif areaSelected == "5":
        
        # Esfera
        print("")
        print("")
        print("Esfera")
        print("")
        print("")
        raio = int(input("Raio: "))
        PI = 3.142
        result = ((PI * (raio * raio * raio)) * (4/3))
        print("Volume: " + str(result))


    else:

        print("Wrong Mode")

def PerimetrosMode():

    print("           ")
    print("           ")
    print("Modo Selecionado")
    print("           ")
    print("Seleciona o Perímetro que queres calcular:")
    print("           ")
    print("1| Quadrado")
    print("2| Retângulo")
    print("3| Polígono Regular")
    print("4| Trapézio")
    print("5| Losângulo")
    print("6| Círculo")
    print("7| Triângulo Escaleno")
    print("8| Triângulo Isósceles")
    print("9| Triângulo Equilátero")
    print("           ")
    
    areaSelected = input("Modo: ")


    if areaSelected == "1":

        # Quadrado
        print("")
        print("")
        print("Quadrado")
        print("")
        print("")
        lado = int(input("Lado: "))
        PI = 3.142
        result = 4 * lado
        print("Perímetro: " + str(result))

    
    elif areaSelected == "2":

        print("-------")
        print("")
        # Retângulo
        print("")
        print("")
        print("Retãngulo")
        print("")
        print("")
        largura = int(input("Largura: "))
        altura = int(input("Altura: "))
        result = 2 * (altura + largura)
        print("Perímetro: " + str(result))
    

    elif areaSelected == "3":

        print("-------")
        print("")
        # Poligono Regular
        print("Poligono Regular")
        print("")
        print("")
        lado = int(input("Lado: "))
        nLados = int(input("Número de Lados: "))
        result = lado * nLados
        print("Perímetro: " + str(result))


    elif areaSelected == "4":
        
        print("-------")
        print("")
        # Trapézio
        print("Trapézio")
        print("")
        print("")
        baseMaior = int(input("Base Maior: "))
        baseMenor = int(input("Base Menor: "))
        lado1 = int(input("Lado 1: "))
        lado2 = int(input("Lado 2: "))
        result = baseMaior + baseMenor + lado1 + lado2
        print("Perímetro: " + str(result))


    elif areaSelected == "5":
        
        print("-------")
        print("")
        # Losângulo
        print("Losângulo")
        print("")
        print("")
        lado = int(input("lado: "))
        result = lado * 4 
        print("Perímetro: " + str(result))


    elif areaSelected == "6":
         
        print("-------")
        print("")
        # Círculo
        print("Círculo")
        print("")
        print("")
        diametro = int(input("Diametro: "))
        Pi = 3.142
        result = diametro * Pi
        print("Perímetro: " + str(result))


    elif areaSelected == "7":
        
        print("-------")
        print("")
        # Triângulo Escaleno
        print("Triângulo Escaleno")
        print("")
        print("")
        a = int(input("Lado A: "))
        b = int(input("Lado B: "))
        c = int(input("Lado C: "))
        PI = 3.142
        resultTotal = a + b + c
        print("Perímetro: " + str(resultTotal))


    elif areaSelected == "8":
            
        print("-------")
        print("")
        # Triângulo Isósceles
        print("Triângulo Isósceles")
        print("")
        print("")
        a = int(input("Lado A: "))
        b = int(input("Lado B: "))
        PI = 3.142
        resultTotal = (2 * b) + a
        print("Perímetro: " + str(resultTotal))


    elif areaSelected == "9":
        
        print("-------")
        print("")
        # Triângulo Equilátero
        print("Triângulo Equilátero")
        print("")
        print("")
        a = int(input("Lado A: "))
        PI = 3.142
        result = 3 * a
        print("Perímetro: " + str(result))
        
    
    else:

        print("Wrong Mode")

def FQMode():

    print("           ")
    print("           ")
    print("Modo Selecionado")
    print("           ")
    print("Seleciona uma Opção:")
    print("           ")
    print("1| Moles/Qta.Matéria/NdeAvogadro ")
    print("           ")
    
    areaSelected = input("Modo: ")


    if areaSelected == "1":

        print("Seleciona uma Opção:")
        print("           ")
        print("1| Número de Partículas (N) ")
        print("2| Quantidade de Matéria (n) ")
        print("3| Número de Matéria (n) (massa) ")
        print("3| Massa Molar ")
        print("  ")














start()

