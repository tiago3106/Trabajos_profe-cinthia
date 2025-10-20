import csv
def verificar_si_existe(nombre):
    try:
        with open(nombre, "r", encoding="utf-8") as archivo_csv:
                esta = True
                return esta
    except FileNotFoundError:
        print("Error no se encontro el archivo")
        esta = False
        return esta
    except Exception as E:
        print(f"ocurrio un error inesperado: {e}")
def imprimir(nombre):
    with open (nombre, "r", encoding="utf-8") as archivo_csv:
        fila = csv.reader(archivo_csv)
        for item in fila:
            print(item)
nombre_columnas = ["nombre","precio"]
continuar = True
while continuar:
    opcion = input("Ingrese una opcion: ")
    opcion = int(opcion)
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del archivo: ")
            if not nombre.endswith(".csv"):
                nombre += ".csv"
            existe = verificar_si_existe(nombre)
            if existe == False:
                print("No existe ese archivo, crearemos uno nuevo con ese nombre")
                with open(nombre, "w", newline="") as archivo_csv:
                    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombre_columnas)
                    escritor_csv.writeheader()
            imprimir(nombre)
        case 2:
            nombre = input("ingrese el nombre del producto: ")
            precio = input("ingrese el precio del producto: ")
        case 3:
            print()
        case 4:
            continuar = False
        case _:
            print("Error esa opcion no existe")