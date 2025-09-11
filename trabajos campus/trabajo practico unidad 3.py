from statistics import mode, median, mean #para el ejercicio 6
#1)Mayoria de edad
edad = int(input("Ingrese su edad: "))#ingresa la edad
if edad >= 18:
    print("Es mayor de edad.")
#2)Aprobado o desaprobado
nota = float(input("Ingrese su nota(0-10): "))
if nota >= 6 and nota <= 10:
    print("Usted aprobo")
elif nota< 6 and nota >= 0:
    print("Usted desaprobo")
else:
    print("Nota no valida")#con los condicionales anteriores me aseguro que este entre 0 y 10
#3)Pares uso de %  
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:#con el numero dividido por 2 y el mod que da el resto veremos si es par o no
    print("El numero es par")
else: 
    print("Por favor, ingrese un numero par")
#4)Categoria segun la edad(niños/adolescentes/adultos jovenes/adultos)
edad = int(input("Ingrese su edad: "))    
if edad < 12:
    print("Eres un niño/a.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un adulto joven")
elif edad > 30:
    print("Eres un adulto")
#5)contraseña entre 8-14 caracteres 
clave = input("Ingrese una clave entre 8 y 14 caracteres: ")
largo = len(clave) #ve cuantos caracteres tiene contando los espacios
if largo >= 8 and largo <=14: #usamos un condicional junto al len para verificar que este entre estos numeros
    print("Su clave es valida")
else:
    print("Ingrese una clave valida")
#6) Muestra que tipo de sesgo tiene una lista generada al azar
from statistics import mode, median, mean #para calcular media, mediana y moda
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]#crea una lista de 50 numeros entre 1-100
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(numeros_aleatorios)
print(f"La media es:\t{media}")
print(f"La mediana es:\t{mediana}")
print(f"La moda es:\t {moda}")
if media > mediana and mediana > moda:
    print("La lista tiene sesgo positivo")
elif media < mediana and mediana < moda:
    print("La lista tiene sesgo negativo")
elif media == mediana and mediana == moda:
    print("La lista no tiene sesgo")
#7) agregar un ! cuando termine en vocal
frase = input("Ingrese una frase o palabra: ").lower()#cambia a minusculas todas las letras de la palabra
if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or frase[-1] == "o" or frase[-1] == "u": #para no usar listas lo hice mas largo
    print(frase + "!")
else:
    print(frase)
#8)transformar de minusculas a mayusculas totales o solo la primera letra
nombre = input("Ingrese su nombre: ")
print("Ingrese 1 si desea que se imprima su nombre en mayusculas.")
print("Ingrese 2 si desea que se imprima su nombre en minusculas.")
print("Ingrese 3 si desea que se imprima su nombre con la primer letra mayuscula.")
opcion= int(input("Ingrese el numero correspondiente a la opcion que desea: "))
if opcion == 1:
    print(nombre.upper())#Pasa toda la palabra a mayusculas
elif opcion == 2:
    print(nombre.lower())#pasa toda la palabra a minusculas
elif opcion == 3:
    print(nombre.title())#pasa la primer letra a mayusculas
#9) pide la magnitud y muestra la escala
escala = float(input("Ingrese la magnitud del terremoto: "))
if escala < 3:#dependiendo de la magnitud muestra una categoria
    print("Categoria muy leve")
elif escala < 4:
    print("Categoria leve")
elif escala < 5:
    print("Categoria moderado")
elif escala < 6:
    print("Categoria fuerte")
elif escala < 7:
    print("Categoria muy fuerte")
elif escala >= 7:
    print("Categoria extremo")    