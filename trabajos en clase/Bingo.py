#bingo 5 x 5 
import random
ganar = 0
filas = 5
columna =5   
num = random.sample(range(1,51),25)
talon = [random.sample(num[i:i+5],5) for i in range(0,25,5)]
print("Bienvenido al Bingo")
print("Tu talon es: ")
for fila in talon:
    print(fila)
while ganar == 0:
    num_sorteados = random.sample(range(1,51),50)
    for numero in num_sorteados:
        print(f"El numero que salio es: {numero}")
        for i in range(filas):
            for j in range(columna):
            print("")
                if talon[i][j] == numero:
                    print(f"¡Número {numero} marcado en tu cartón!")
                    talon[i][j] = 0
                    print(talon)
            print("")
    if all(all(x == 0 for x in fila) for fila in talon):
        print("¡Bingo en el cartón!")
        ganar = 1