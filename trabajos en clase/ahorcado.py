import random
palabras= ["maxi","Matias","tiago"]
condicion_salida = True
while condicion_salida:
    print("----menu----")
    print("opcion 1. jugar")
    print("opcion 2. salir")
    opcion = input("Ingrese el numero de la opcion:")

    match opcion:
        case 1:
            incognita = random(palabras)
            
            
            print("f")
        case 2:
            print(4)
        case _:
            print("Error verifique que lo escribio bien")

def crear_el_doppler(doppler:int):
    
    largo = len(incognita)