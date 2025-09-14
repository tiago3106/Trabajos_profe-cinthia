#Trabajo practico unidad 4
import random
#1) imprimir numeros del 1 al 100
for numero in range (1,101):
    print(numero)
#2) cantidad de digirtos en un numero
num = int(input("Ingrese un numero: "))
contador = 0
while num != 0:
    num = num //10
    contador += 1
print("La cantidad de digitos es: ", contador)
#3)suma de numeros sin contar 
resultado = 0
num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
for numero in range (num_1+1,num_2):
    resultado = numero + resultado
print (resultado)
#4)suma de numeros enteros y salir al 0
suma = 0
print("Ingrese numeros para sumar, si ingresa 0 se detendra el programa")   
while True:
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    suma += num
print("La suma total es: ", suma)
#5) el usuario debe adivinar un numero entre el 0 y 6
contador = 0
numero_aleatorio = random.randint(0,6)
while True:
    numero_elegido = int(input("Adivine el numero entre 0 y 6: "))
    contador += 1
    if numero_elegido == numero_aleatorio:
        print("Felicidades, adivinaste el numero en ", contador, "intentos")
        break
#6)mostrar todos los números pares entre 0 y 100, en orden decreciente.
for numero in range (100,-1,-1):
    if numero % 2 == 0:
        print(numero)
#7)suma de todos los números entre 0 y un número entero positivo dado por el usuario.
num = -1
while num < 0:
    num = int(input("Ingrese un numero entero positivo: "))
suma = 0
for numero in range (num+1):
    suma += numero
print("La suma de todos los numeros entre 0 y ", num, "es: ", suma)
#8)ingresas 100 numeros y el usuario te muestras cuantos son pares/inpareso/negativos/positivos
cantidad_pares = 0
cantidad_impares = 0    
cantidad_positivos = 0
cantidad_negativos = 0
for i in range (100):
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        cantidad_positivos += 1
    elif numero < 0:
        cantidad_negativos += 1
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1   
print("Cantidad de numeros pares: ", cantidad_pares)
print("Cantidad de numeros impares: ", cantidad_impares)
print("Cantidad de numeros positivos: ", cantidad_positivos)
print("Cantidad de numeros negativos: ", cantidad_negativos) 
#9) media de 100 valores
media = 0
suma_total = 0
numero = 0
for i in range (100):
    numero = int(input("Ingrese un numero: "))
    suma_total = suma_total + numero
media = suma_total / 100
print("La media de los 100 numeros es: ", media)
#10) invertir numeros
num = int(input("Ingrese un número para invertir sus dígitos: "))
invertido = 0
while num != 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print("El número invertido es:", invertido)
