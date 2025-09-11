#bingo 5 x 5 
import random
ganar = False
filas = 5   
num = random.sample(range(1,51),25)
talon = [random.sample(num[i:i+5],5) for i in range(0,25,5)]
print("Bienvenido al Bingo")
print("Tu talon es: ")
for fila in talon:
    print(fila)