
def imprimir_hola_mundo():
    print("Hola, Mundo!")
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
def calcular_area_circulo(radio): 
    area = 3.1416 * radio * radio
    return area 
def calcular_perimetro_circulo(radio) : 
    perimetro = 2 * 3.1416 * radio
    return perimetro
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
#1)
imprimir_hola_mundo()
#2)
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)
#3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#4)
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area} y el  perímetro es: {perimetro}")
#5)
segundos = float(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas")
#6)
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)
#7) def operaciones_basicas(a, b) que reciba
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")
#8)
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)
#9)
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
#10)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es {promedio}")