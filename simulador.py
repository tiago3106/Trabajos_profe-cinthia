#creado para cuando tenga que hacer varios algoritmo
escala = float(input("Ingrese la magnitud del terremoto: "))
if escala < 3:
    print("Categoria muy leve")
elif escala < 4:
    print("Categoria leve")
elif escala < 5:
    print("Categoria moderado")
elif escala < 6:
    print("Categoria fuerte")
elif escala < 7:
    print("Categoria muy fuerte")
elif escala >= 7:
    print("Categoria extremo")