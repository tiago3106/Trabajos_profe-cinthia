menu = True
mochila = []
repetir = True
while repetir:
    try:
        cantidad_espacio = int(input("Ingrese la capacidad de espacio que tiene su mochila: "))
        if cantidad_espacio > 0:
            for item in range (0,cantidad_espacio):
                mochila.append("---vacio---")
            repetir = False
        else:
                print("Error no se pueden agragr numeros iguales o menores a 0")
    except ValueError:
        print("Error solo puede agregar numeros")
while menu:
    print("1. Guardar objeto")
    print("2. Ver mochila")
    print("3. Salir")
    try:
        opcion = int(input ("Ingrese una opcion: "))
    except ValueError:
        print("Error no puede ingresar un numero")
    match opcion:
        case 1:
            try:
                buscar = int(input("En que posicion deseas agregar tu objeto: "))
            except ValueError:
                print("Error solo puede agregar numeros")
            try: 
                mochila[buscar]
                colocar = input("Que desea agregar a la mochila: ").lower()
                mochila[buscar] = colocar
            except IndexError:
                print("Error no existe ese indice")
        case 2:
            for item in range(0,cantidad_espacio):
                print(mochila[item])
        case 3:
            mochila = False