#TP_1_campus
#Tiago Guillot Duran
#1)Imprime hola mundo
print("Hola Mundo!")
#2) El usuario introduce un nombre y el algoritmo lo devuelve con un saludo
nombre = input("Ingrese su nombre: ")
print(f"Saludos {nombre}")
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese un pais: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y soy de {pais}.")
#5) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
print ("Bienvenido a la calculadora de area y perimetros del circulo.")
radio = float(input("Ingrese el radio del circulo: "))
perimetro = 2*radio*3.14
area = 3.14 * radio*radio
print (f"Basandonos en el radio: {radio} nos dio que ")
print (f"el area del circulo es {area} y el perimetro es {perimetro}")
#6)pide al usuario que diga una cantidad de segundos y imprimo el equivalente en horas
segundos = int(input("Ingrese la cantidad de segundos para pasarlos a horas: "))
horas = segundos / 3600
print(f"La cantidad de horas equivalentes a {segundos} segundos son {horas} horas.")
#7) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int(input("Introduce un numero para calcular su tabla de multiplicar: "))
print (f"{numero} x 1 = {numero}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 10 = {numero * 10}")
#8) pedir peso y altura para calcular el IMC = masa en kg / altura en m*m
print("Calculadora de Indice de masa corporal ")
masa = float(input("Introduce tu peso en kg y max 2 decimales: "))
altura = float(input("Ingrese su altura en m y maximo 2 decimales:"))
Indice_de_masa_corporal = masa / (altura* altura)
print (f"Tu indice de masa corporal es: {Indice_de_masa_corporal}.")
#9) conversion celcius a fahrenheit
Temperatura_celcius = float(input("Introduzca la temperatura en celcius: "))
Temperatura_fahrenheit = (9/5)* Temperatura_celcius + 32
print (f"La temperatura equivale a {Temperatura_fahrenheit}")
#10) pedir 3 numeros y calcular su promedio
nota_1 = int(input("Ingrese la primer nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))
promedio = (nota_1 + nota_2 + nota_3)/3
print (f"El promedio es {promedio}.")