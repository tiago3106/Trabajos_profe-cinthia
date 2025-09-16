#Caso 1
terminar = True
titulos= [] #creo una lista para los titulos
ejemplares = [] #una lista para la cantidad de ejemplares
while terminar:
    print("Bienvenido a la biblioteca escolar ")
    print("Opcion(1) agregar titulos")
    print("Opcion(2) agregar ejemplares por titulo")
    print("Opcion(3) mostrar catalogo con stock")
    print("Opcion(4) consultar un titulo")
    print("Opcion(5) lista de agotados")
    print("Opcion(6) agregar un titulo con ejemplar")
    print("Opcion(7) actualizar ejemplares")
    print("Opcion(8) ver catalogo")
    print("Opcion(9) salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:
        condicion = True
        while condicion: #bucle para agregar indefinidamente titulos de libros
            nuevo_libro = input("Introduce el nombre del libro al catalogo: ")
            titulos.append(nuevo_libro) #se agrega el nuevo titulo a la lista
            salir = input("Desea agregar mas libros (s/n): ").lower()
            if salir == "n":
                condicion = False     
    elif opcion == 2:
        if len(titulos) == 0:
            print("Error primero introduce algun titulo")
            continue
        else:
            largo = len(titulos)
            condicion = True
            print(titulos)
            while condicion: #bucle para agregar indefinidamente ejemplares
                    libro_agregar_ejemplares = input("Introduce el nombre del libro al que diras la cantidad de ejemplares: ") #el nombre del libro 
                    for iteracion in range(0,largo):
                        if libro_agregar_ejemplares == titulos[iteracion]:
                            cantidad_de_ejemplares = int(input("Introduce la cantidad de ejemplares: "))
                            ejemplares.append(cantidad_de_ejemplares) #se agrega el numero de ejemplares
                    salir = input("Desea agregar mas ejemplares(s/n): ").lower()
                    if salir == "n":
                        condicion = False
    elif opcion == 3:
        largo = len(titulos) #guarda la cantidad de elementos en una lista
        print("Catalogo / stock")
        for iteracion in range(0,largo): #nos muestra el catalogo disponible
            print(f"{titulos[iteracion], ejemplares[iteracion]}")
        
    elif opcion == 4:
        print("Encontrar ejemplares de un libro")
        condicion = True
        while condicion: #busca si el libro esta en la lista y te muestra cuantos ejemplares hay
            consulta_titulo = input("Introduce el libro que deseas buscar: ")
            indice = titulos.index(consulta_titulo)
            print(f"Hay {ejemplares[indice]} ejemplares disponibles")
            salir = input("Desea consultar mas libros (s/n): ").lower()
            if salir == "n":
                condicion = False   
    elif opcion == 5: 
        print("Catalogo de libros no disponibles")
        for iteracion in range(0,largo): #muestra cauntos libros hay con 0 ejemplares
            if ejemplares[iteracion] == 0:
                print(f"Hay cero ejemplares de {titulos[iteracion]}")
        print("")
    elif opcion == 6:
        print("Agregar libro y ejemplares del mismo")
        condicion = True
        while condicion: # introducir mas libros
            nuevo_libro = input("Introduce el nuevo libro al catalogo: ")
            titulos.append(nuevo_libro)
            nuevo_ejemplar = input("Introduce la cantidad de ejemplares: ")
            ejemplares.append(nuevo_ejemplar)
            salir = input("Desea agregar otro libro(s/n): ").lower()
            if salir == "n":
                condicion = False
    elif opcion == 7:
        print("Actualizar ejemplares")
        condicion = True
        while condicion:
            opcion = input("Desea devolver(d) o llevarse prestado(p) un libro: ").lower() #elige si desea devolver o llevarse
            if opcion == "p":
                prestado = input("Que libro desea llevarse: ")
                indice = titulos.index(prestado)
                cantidad = int(ejemplares[indice])
                ejemplares[indice] = cantidad - 1
                salir = input("Desea lleavarse otro libro(s/n): ")
            if opcion == "d":
                devolver = input("Que libro desea devolver: ")
                indice = titulos.index(devolver)
                cantidad = ejemplares[indice]
                ejemplares[indice] = cantidad + 1
                salir = input("Desea devolver otro libro(s/n): ")
                if salir == "n":
                    condicion = False
                    
    elif opcion == 8:
        largo = len(titulos)
        print("catalogo")
        for iteracion in range(0,largo): #muestra el catalogo actualizado
            print(f"Tenemos {titulos[iteracion]}, {ejemplares[iteracion]} disponibles.")
    else:
        condicion = input("Si desea terminar escriba (n) sino escriba cualquier cosa: ").lower()
        break
