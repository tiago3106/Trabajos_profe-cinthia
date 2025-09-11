#Empiezo
dia_semana, dia, mes = input("ingrese el dia de la semana/dia/mes: ").split("/")
#cambiamos a minusculas para que no salte error si lo puso en mayusculas
dia_semana = str(dia_semana.lower())
dia = int(dia)
mes = int(mes)
fecha_valida = bool(True)
#verificamos que los dias si sean de entre la semana
if (dia_semana != "lunes") and (dia_semana != "martes") and (dia_semana != "miercoles") and (dia_semana != "jueves" ) and (dia_semana != "viernes"):
    fecha_valida = False
#verificamos que no ponga un mes que no exista
if (mes > 12):
    fecha_valida = False
#verificamos que no ponga un 32
if (mes == "01") or (mes == "03") or (mes == "05") or (mes == "07") or (mes == "08") or (mes == "10") or (mes == "12"):
    if (dia > "31"):
        fecha_valida = False
#verificamos que no ponga un 31 en adelante 
if (mes == "04") or (mes == "06") or (mes == "09") or (mes == "11"):
    if (dia > "30"):
        fecha_valida = False
#verificamos que en febrero no ponga mas que 29
if (mes == "02"):
    if (dia >29):
        fecha_valida = False
#si sale falso alguna de los anteriores que salte error
if fecha_valida == False:
    print ("Syntax error fecha no valida.")

# lunes = nivel inicial, martes = nivel intermedio, miercoles avanzado, jueves practica hablada
# viernes se dicta ingles para viajeros
#Examenes solo el nivel inicial,intermedio,avanzado pregutar si tuvo, preguntar cuantos aprobaron y cuantos no y calcular el porcentaje de aprobados
#si el jueves ingresa porcentaje de asistencia si es > 50% escribir asistio la mayoria sino escribir no asistio la mayoria
# si es viernes y es 1 de enero o julio se imprime "comienzo de nuevo ciclo"
#Solicitar al usuario la cantidad de ingresantes y el arancel $ por cada alumno imprimir el total
if (dia_semana == "lunes") or (dia_semana == "martes") or (dia_semana == "miercoles"):
    examenes = input("Tuvieron examen hoy: ")
    examenes.lower()
    if (examenes == "si"):
        aprobados = int(input("Cuantos aprobaron?: "))
        desaprobados = int(input("Cuantos desaprobaron: "))
        print("Aprobaron un ", (aprobados/aprobados+desaprobados), "%")
elif (dia_semana == "jueves"):
    asistencia = float(input("(Ingrese el porcentaje de asistencia en decimal 20% ==  0.2): "))
    asistencia = asistencia * 100
    if asistencia > 50:
        print("Asistio la mayoria")
    elif asistencia< 50:
        print("No asistio la mayoria")
    elif asistencia == 50:
        print("Asistio la mitad")
if (dia_semana == "viernes"):
    if (mes == 1) or (mes == 7):
        if (dia == 1) :
            print("Comienzo de nuevo ciclo")
            cantidad_ingresantes = int(input("Ingrese la cantidad de alumnos ingresantes: "))
            aranceles = int(input("Ingrese el arancel mensual por alumno: "))
            total = cantidad_ingresantes * aranceles
            print (f"la cantidad total seria de {total}")

print ("Hasta pronto")