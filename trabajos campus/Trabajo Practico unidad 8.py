#Trabajo Practico unidad 8
#1)
with open ("producto.txt", "w") as archivo:
    archivo.write ("nombre, precio, cantidad\n")
    print("Archivo creado con éxito.")
#2)
with open ("producto.txt", "r") as archivo:
    lista = archivo.readline().strip()
    for linea in archivo:
        nombre = linea.strip().split(",")
        print(nombre)
        print(f"Producto: {nombre[0]}, Precio: {nombre[1]}, Cantidad: {nombre[2]}")
#3)
with open ("producto.txt", "a") as archivo:
    continuar = True
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        archivo.write(f"{nombre},{precio},{cantidad}\n")
        print("Producto agregado con éxito.")
        salir = input("¿Desea agregar otro producto? (s/n): ")
        if salir.lower() != "s":
            break
#4)
    
productos = {}
with open("producto.txt", "r") as archivo:
    next(archivo)  # Saltar la primera línea (encabezado)0
    for linea in archivo:
        nombre = linea.strip().split(",")
        productos = {"nombre": nombre[0], "precio": float(nombre[1]), "cantidad": int(nombre[2])}
    print(productos)
#5)
with open("producto.txt", "r") as archivo:
    next(archivo)  # Saltar la primera línea (encabezado)
    productos = archivo.readlines()
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for linea in productos:
        if lineax[0].lower() == nombre.lower():
            print(f"Producto encontrado: {linea.strip()}")
            break
    else:
        print("Producto no encontrado.")
