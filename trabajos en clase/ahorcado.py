import random
def crear_el_tablero(palabra:int):
    largo = len(palabra)
    for letra in range(0,largo):
        escondido.append("_")
    return escondido
def buscar_letra(letra:str,intentos):
    largo = len(palabra)
    bandera = True
    for letra_en_palabra in range (0,largo):
        if letra == palabra[letra_en_palabra]:
            escondido[letra_en_palabra] = letra
            bandera = False
    if bandera == True:
        print(f"No se encontro ninguna {letra} en la palabra")
        intentos = intentos - 1
    letras.append(letra)
    return intentos
def verificar(escondido, ganar):
    contador = 0
    largo = len(escondido)
    for item in range (0,largo):
        if escondido[item] == "_":
            contador += 1
    if contador == 0:
        ganar = True
        return ganar

palabras = ["verde","amarillo","rojo","azul","rosa","magenta","bordo","celeste"]
condicion_salida = True
while condicion_salida:
    print("----menu----")
    print("opcion 1. jugar")
    print("opcion 2. salir")
    escondido = []
    opcion = input("Ingrese el numero de la opcion: ")
    if not opcion.isdigit():
        print("Error solo se pueden ingresar numeros")
        continue
    opcion = int(opcion)
    match opcion:
        case 1:
            letras = []
            intentos = 7
            ganar= False
            juego = True
            palabra = random.choice(palabras)
            print(palabra)
            crear_el_tablero(palabra)
            print("Bienvenido la categoria es colores")
            while juego:
                print("")
                print(f"Adivina el color  {escondido}")
                print(f"Le quedan {intentos} aciertos")
                print(f"Letras usadas {letras}")
                letra = input("Ingrese una letra: ").lower()
                if len(letra) >1 or len(letra) <1:
                    print("Error solo puede agregar una letra")
                    continue
                if letra < "a" or letra > "z":
                    print("Error solo puede agregar letras de la a la z (la ñ tampoco se puede)")
                    continue
                intentos = buscar_letra(letra,intentos) 
                ganar = verificar(escondido,ganar)
                if ganar == True:
                    print("Felicidades adivinaste el color")
                    juego = False
                if intentos == 0:
                    print("Perdiste te quedaste sin intentos")
                    juego = False
            continuar = True
            while continuar:
                salir = input("Desea jugar otra ronda (s/n): ").lower()
                if salir == "n":
                    break
                elif salir == "s": 
                    print("De acuerdo, volviendo al menu")
                else:
                    print("Error solo puede ingresar (s) o (n)")
                    continue
                continuar = False
        case 2:
            condicion_salida = False
        case _:
            print("Error verifique que escribio bien el numero")