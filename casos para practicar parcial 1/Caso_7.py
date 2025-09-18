Menu = True
Bandera = False
continuar = True
Alumnos = []
Asistencias = []
while Menu:
    print("Ingrese el numero de La opcion que desea: ")
    print("1. Agregar lista de estudiantes")
    opcion = input("Ingrese la opcion que desea: ")
    if opcion == "1":
        while continuar:
            Nombre = input("Ingrese el nombre del alumno: ")
            Alumnos.append(Nombre)
            Asistencias.append(0)
            salir = input("Desea salir (s/n): ").lower()
            if salir == "s":
                continuar = False
    if opcion == "2":
        Nombre = input("Ingrese el nombre del alumno: ")
        Alumnos.append(Nombre)
        Asistencias.append(0)
    if opcion == "3":
        largo = len(Alumnos)
        for i in range(0,largo):
            print(f"El {Alumnos[i]}, tiene {Asistencias[i]} ")
    if opcion == "4":
        continuar = True
        largo = len(Alumnos)
        while continuar:
            Buscador_de_alumnos = input("Ingrese el nombre del alumnos: ")
            for i in range(0,largo):
                if Buscador_de_alumnos == Alumnos[i]:
                    print (f"El alumno {Alumnos[i]} tiene {Asistencias[i]}.")
                    bandera = True
                    continuar = False
            if bandera == False:
                continuar = True
    if opcion == "5":
        continuar = True
        bandera = False
        largo = len(Alumnos)
        while continuar:
            Buscador_de_alumnos = input("Ingrese el nombre del alumnos: ")
            for i in range(0,largo):
                if Asistencias[i] == 0:
                    print (f"El alumno {Alumnos[i]} tiene {Asistencias[i]}.")
                    bandera = True
                    continuar = False
            if bandera == False:
                continuar = True
    if opcion == "6":
        continuar = True
        bandera = False
        largo = len(Alumnos)
        while continuar:
            Buscador_de_alumnos = input("Ingrese el nombre del alumnos que asistio: ")
            for i in range(0,largo):
                if Buscador_de_alumnos == Alumnos[i]:
                    numero = Asistencias[i]
                    numero += 1
                    Asistencias[i]= numero
                    bandera = True
                    continuar = False
            if bandera == False:
                continuar = True


