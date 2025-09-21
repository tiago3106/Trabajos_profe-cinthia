Mantener = True
especializacion = []
cupos=[]
while Mantener:
    bandera = False
    print("1.	Ingresar lista de especialidades")
    print("2.	Ingresar lista de cupos disponibles por especialidad")
    print("3.	Mostrar agenda: ")
    print("4.	Consultar cupos de una especialidad: ")
    print("5.	Listar especialidades sin cupo: ")
    print("6.	Agregar especialidad")
    print("7.	Actualizar cupos (reservar/cancelar): ")
    print("8.	Salir")
    opcion = input("Ingrese el numero de la opcion: ")
    if not opcion.isdigit():
        print("Error: Debe ingresae un numero valido")
        continue
    opcion = int(opcion)
    match opcion:
        case 1:
            repeticion = 1
            while repeticion == 1:
                nueva_especialidad = input("Ingrese la especialidad: ")
                especializacion.append(nueva_especialidad)
                cupos.append(0)
                salir = input("Quiere agregar mas especialidades(s/n): ").lower()
                if salir == "n":
                    repeticion = 0
        case 2:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            repeticion = 1
            while repeticion == 1:
                print(especializacion)
                buscar_especialidad = input("Escriba la especialidad a la que quiere agregar cupos: ")
                largo = (len(especializacion))
                for iteracion in range(0,largo):
                    if buscar_especialidad == especializacion[iteracion]:
                        agregar_cupos = int(input(f"Ingrese la cantidad de cupos para la especialidad {especializacion[iteracion]}:"))
                        cupos[iteracion] = agregar_cupos
                        bandera = True
                        salir = input("Quiere agregar mas cupos(s/n): ").lower()
                        if salir == "n":
                            repeticion = 0  
                if bandera == False:
                    print("No se encontro el nombre  verifique que este bien escrito")                  
        case 3:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            largo = len(especializacion)
            for agenda in range(0,largo):
                print(f"Tenemos {cupos[agenda]} de {especializacion[agenda]}")
        case 4:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            repeticion = 1
            while repeticion == 1:
                print(especializacion)
                buscar_especialidad = input("Escriba la especialidad que quiere saber disponibilidad: ")
                largo = len(especializacion)
                for iteracion in range(0,largo):
                    if buscar_especialidad == especializacion[iteracion]:
                        print(f"{especializacion[iteracion]} tiene {cupos[iteracion]} cupos.")
                        bandera = True
                        salir = input("Quiere agregar mas cupos(s/n): ").lower()
                        if salir == "n":
                            repeticion = 0 
                if bandera == False:
                    print("No se encontro la especialidad asegurese de que este bien escrito")                   
        case 5:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            largo = len(especializacion)
            for esp in range (0,largo):
                if cupos[esp] == 0:
                    print(f"{especializacion[esp]} tiene {cupos[esp]} cupos")
                    bandera = True
            if bandera == False:
                print("No se encontraron especialidades con cero cupos")
        case 6:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            repeticion = 1
            while repeticion == 1:
                nueva_especialidad = input("Ingrese la especialidad: ").split()
                if especializacion == "":
                    print("Error tiene que introducir una palabra")
                    continue
                existe = False
                for t in range(especializacion):
                    if t.lower() == nueva_especialidad:
                        existe = True 
                        break
                if existe:
                    print("Error esa especialidad ya existe")
                    continue
                especializacion.append(nueva_especialidad)
                agregar_cupos = int(input("Ingrese la cantidad de cupos: "))
                cupos.append(agregar_cupos)
                salir = input("Quiere agregar mas especialidades(s/n): ").lower()
                if salir == "n":
                    repeticion = 0
        case 7:
            largo = len(especializacion)
            if largo <= 0:
                print("Error: Primero ingrese la opcion 1 ")
                continue
            repeticion = 1
            while repeticion == 1:
                elecion = input("Desea reservar(r) o cancelar(c) un cupo")
                if elecion == "r":
                    print(especializacion)
                    buscar_especialidad = input("Escriba la especialidad que quiere resevar: ")
                    largo = len(especializacion)
                    for iteracion in range(0,largo):
                        if buscar_especialidad == especializacion[iteracion]:
                            print("Listo ya le reservamos el lugar")
                            cantidad = cupos[iteracion]
                            cantidad -= 1
                            cupos[iteracion] = cantidad
                            bandera = True
                            salir = input("Quiere modificar algun otro cupo(s/n): ").lower()
                            if salir == "n":
                                repeticion = 0
                    if bandera == False:
                        print("No se encontro la especializacion verifique que la escribiera bien")                    
                elif elecion == "c":
                    print(especializacion)
                    buscar_especialidad = input("Escriba la especialidad que quiere cancelar: ")
                    largo = len(especializacion)
                    for iteracion in range(0,largo):
                        if buscar_especialidad == especializacion[iteracion]:
                            print("Listo ya le cancelamos el lugar")
                            cantidad = cupos[iteracion]
                            cantidad += 1
                            cupos[iteracion] = cantidad
                            salir = input("Quiere modificar algun otro cupo(s/n): ").lower()
                            bandera = True
                            if salir == "n":
                                repeticion = 0 
                    if bandera == False:
                        print("No se encontro la especializacion verifique que la escribiera bien")
                else:
                    print("Error, asegurese de poner r para reservar o c para cancelar")
        case 8:
            salir = ("Desea salir (s/n): ").lower()
            if salir == "s":
                break
        case(_):
            print("Error sintax")
            print("Asegurese de escribir bien el numero")