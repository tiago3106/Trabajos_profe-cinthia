laberinto = [
    ['D', '#', '#', '#', '#'],
    ['_', '_', '#', '_', '_'],
    ['#', '_', '_', '_', '#'],
    ['#', '_', '#', '_', '_'],
    ['#', '_', '#', '#', 'S'],
]
def movimiento():
    print("4 para la izquierda, \n 8 para arriba \n 6 para la derecha \n 2 para abajo")
    moverse = input("Ingrese a que lado se mueve")
    
def ubicacion_dragon(laberinto):
    for i in range (0,len(laberinto)):
        posicion = laberinto[i].index("D")
        print(i,posicion)
        return posicion
ubicacion_dragon(laberinto)


