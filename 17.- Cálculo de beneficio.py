precio_venta = input("Ingrese el precio del producto:")
cant_vendida = input("Ingrese cuantas unidades se vendieron:")
costo_fijo = input("Ingrese el costo fijo del producto:")
costo_variable = input ("Ingrese el costo variable del pruducto:")

beneficio = float(precio_venta) - float(costo_variable) * float(cant_vendida) - float(costo_fijo)
print(f"El beneficio total es de {beneficio} pesos")