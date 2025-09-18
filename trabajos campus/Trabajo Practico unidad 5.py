#Trabajo practico Nº5 (listas)
#1) usando listas imprimir los multiplos de 4 del 1 al 100
multiplos_de_cuatro = []
for num in range(1,101):
    if num % 4 == 0:
        multiplos_de_cuatro.append(num)
#2) crear una lista con 5 elementos
lista_elementos= ["corpus", "gatos", "hombres", "magic", "zumba"]
print(lista_elementos[-2])
#3)crear una lista vacia y agregar 3 valores
lista_3=[]
for i in range (3):
    agregar = input("Ingrese un elemento a la lista: ")
    lista_3.append(agregar)
print(lista_3)
#4) en el segundo y el ultimo valor cambiarlos por loro y oso respectivamente
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)
#5) crea una variable con numeros
#con el max() busca la variable con el numero mas grande y lo elimina y vuelve a mostrar la lista modificada

#6)una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros
lista_6 = []
for num in range(10,31,5):
    lista_6.append(num)
print(lista_6[0],lista_6[1])
#7) remplazar los valores de auto indice 1,2
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "patos"
autos[2] = "gatos"
print(autos)
#8) lista dobles y poner el doble de 5,10,15
Dobles=[]
for num in range (5,16,5):
    Dobles.append(num+num)
print(Dobles)
#9) cambiar cosas de la lista
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#c) Eliminar "pan" de la lista del primer cliente.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[0].remove("pan")
compras[1][1] = "tallarines"
print(compras)
#10) lista anidada
lista_anidada= ["","",["","",""],""]
lista_anidada[0]= 15
lista_anidada[1]= True
lista_anidada[2][0]= 25.5
lista_anidada[2][1]= 57.9
lista_anidada[2][2]= 30.6
lista_anidada[3]= False
print(lista_anidada)



