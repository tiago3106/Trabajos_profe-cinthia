total = int(input("Ingrese el monto total de la cuenta: "))
propina_diez = total * 0.1
propina_quince = total *0.15
total_propina_diez = total + propina_diez
total_propina_quince = total + propina_quince
print(f"El total sin propina es:\t${total}")
print(f"El 10% de propina es:\t\t${propina_diez}")
print(f"El 15% de propina es:\t\t${propina_quince}")
print(f"El total con propina es:\t${total_propina_diez}")
print(f"El total con propina es:\t${total_propina_quince}")