#1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"] = 15000
precios_frutas["Pera"] = 2300
print(precios_frutas)
#2)
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)
#3)
frutas = list(precios_frutas.keys())
print(frutas)
#4)
agenda = {}  # usar diccionario, no tupla
cantidad = input("¿Cuántos números deseas agregar? ")
if not cantidad.isdigit():
    print("Ingrese un número válido")
else:
    cantidad = int(cantidad)
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del contacto: ").strip()
        numero = input("Ingrese el número del contacto: ").strip()
        agenda[nombre] = numero
    
print(agenda)
consulta = input("Ingrese el nombre del contacto a buscar: ").strip()
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
#6)
frase = input("Ingrese una frase: ")
palabras_unicas = {}
for palabra in frase.split():
    palabras_unicas[palabra] = palabras_unicas.get(palabra, 0) + 1
print(palabras_unicas)
#7)
alumnos = {}
for name in range(0,0):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    nota_2 = float(input("Ingrese la segunda nota del alumno: "))
    nota_3 = float(input("Ingrese la tercera nota del alumno: "))
    alumnos[nombre] = (nota, nota_2, nota_3)
    promedio = (nota + nota_2 + nota_3) / 3
    print(f"El promedio de {nombre} es {promedio}")
#8)
notas_parcial_1 = {"mateo": 7, "juan": 3, "ana": 9, "luis": 8}
notas_parcial_2 = {"mateo": 8, "juan": 7, "ana": 0, "luis": 4}
print("Alumnos que aprobaron ambos parciales:")
for alumno in notas_parcial_1:
    if notas_parcial_1[alumno] >= 6 and notas_parcial_2[alumno] >= 6:
        print(alumno)
print("alumnos que aprobaron solo un parcial:")
for alumno in notas_parcial_1:
    if (notas_parcial_1[alumno] >= 6 and notas_parcial_2[alumno] < 6) or (notas_parcial_1[alumno] < 6 and notas_parcial_2[alumno] >= 6):
        print(alumno)
print("Alumnos que aprobaron al menos un parcial:")
for alumno in notas_parcial_1:
    if notas_parcial_1[alumno] >= 6 or notas_parcial_2[alumno] >= 6:
        print(alumno)
#9)
agenda = {}
while True:
    dia_semana,hora = input("Ingrese el (dia,hora) con coma en medio: ").split(",")

    Asunto = input("Ingrese el asunto de la reunión: ")
    agenda[(dia_semana, hora)] = Asunto    
    salir = input("Si desea salir, ingrese 'salir', de lo contrario presione Enter: ")
    if salir.lower() == 'salir':
        break 
print("Agenda de reuniones:")
#10)
normal = {"argentina": 'Buenos Aires', "brasil": 'Brasilia', "chile": 'Santiago', "colombia": 'Bogotá'}
inversa = {valor: clave for clave, valor in normal.items()}
print("Diccionario normal: ", normal)
print("Diccionario inverso: ", inversa)