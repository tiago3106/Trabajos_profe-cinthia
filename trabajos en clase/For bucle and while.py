#For bucle for
cantidad_de_corridas = int(input("Introduce cuantas casillas se movera: "))
oficiales = 5
jefes = 1
abecedario = ["a","b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
palabra_nueva = ""
for oficiales in range(5):
    palabra = input("Introduzca la frase: ").lower() 
    for letra in palabra:
        if letra in abecedario:
            posicion = abecedario.index(letra)
            letra_siguiente = abecedario[(posicion + cantidad_de_corridas)%27]
            palabra_nueva += letra_siguiente
        else:
            palabra_nueva +=  letra
    print(palabra_nueva)
    palabra_nueva = ""

#bucle while
import random
juego = "entrar"
mini_juego = ["piedra", "papel", "tijera"]
cuenta_ganadas = 0
cuenta_perdida = 0
while juego != "salida":
    print("Bienvenido a piedra, papel o tijera")
    print("introduzca (1) para piedra")
    print("introduzca (2) para papel")
    print("introduzca (3) para tijera")
    player_1 = input("Introduce tu jugada: ")
    elecion = mini_juego[int(player_1) - 1] if player_1 in ["1", "2", "3"] else "Entrada no válida"
    player_2 = random.choice(mini_juego)
    print(f"El jugador 1 ha elegido {elecion}")
    print(f"El jugador 2 ha elegido {player_2}")
    if elecion == player_2:
        print("Empate")
    elif (elecion == "piedra" and player_2 == "tijera") or (elecion == "papel" and player_2 == "piedra") or (elecion == "tijera" and player_2 == "papel"):
        print("Gana el jugador 1")
        cuenta_ganadas += 1
    elif elecion not in mini_juego:
        print("No has introducido una jugada válida")
    else:
        print("Gana el jugador 2")
        cuenta_perdida +=1  
    print(f"Has ganado {cuenta_ganadas} veces y has perdido {cuenta_perdida} veces")
    juego = input("Si desea salir escribe \"salida\" si no escribi cualquier cosa: ").lower()