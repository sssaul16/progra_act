nombre = input("¿Como te gustaria que te llame?")
precio = input("Ingrese el precio del producto:")
tasa_iva = 16


IVA = float(precio) * tasa_iva / 100
total = float(precio) + IVA
print(f"{nombre}, el precio con IVA es de {total} pesos")