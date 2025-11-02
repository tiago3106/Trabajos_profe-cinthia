#Trabajo Practico unidad 9
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
def decimal_a_binario(decimal):
    if decimal == 0:
        return 0
    else:
        return decimal_a_binario(decimal // 2) * 10 + decimal % 2
def es_palindromo(palabra):
    # normalizar: quitar no alfanuméricos y pasar a minúsculas
    s = ''.join(ch.lower() for ch in palabra if ch.isalnum())

    def helper(i, j):
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        return helper(i + 1, j - 1)

    return helper(0, len(s) - 1)
def sum_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digitos(n // 10)
def contar_bloques(bloques):
    if bloques == 1:
        return 1
    else:
        return bloques + contar_bloques(bloques - 1)
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta = 1 if numero % 10 == digito else 0
        return cuenta + contar_digito(numero // 10, digito)
#1)
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
#2)
posicion = int(input("Ingrese la posición en la secuencia de Fibonacci: "))
fibo_resultado = fibonacci(posicion)
print("El número en la posición", posicion, "de la secuencia de Fibonacci es:", fibo_resultado)
#3)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
potencia_resultado = potencia(base, exponente)
print(base, "elevado a la potencia de", exponente, "es:", potencia_resultado)
#4)
decimal_numero = int(input("Ingrese un número decimal para convertir a binario: "))
binario_resultado = decimal_a_binario(decimal_numero)
print("El número decimal", decimal_numero, "en binario es:", binario_resultado)
#5)
palabra_input = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra_input):
    print("La palabra", palabra_input, "es un palíndromo.")
else:
    print("La palabra", palabra_input, "no es un palíndromo.")
#6)
numero_digitos = int(input("Ingrese un número para sumar sus dígitos: "))
suma_resultado = sum_digitos(numero_digitos)
print("La suma de los dígitos de", numero_digitos, "es:", suma_resultado)
#7)
bloques_input = int(input("Ingrese el número de bloques de la base: "))
total_bloques = contar_bloques(bloques_input)
print("El número total de bloques en la pirámide es:", total_bloques)
#8)
numero_contar = int(input("Ingrese un número para contar las apariciones de un dígito: "))
digito_contar = int(input("Ingrese el dígito a contar: "))
apariciones = contar_digito(numero_contar, digito_contar)
print("El dígito", digito_contar, "aparece", apariciones, "veces en el número", numero_contar)