nom_evento = input ('Nombre del evento:')
fecha_evento = input ('Fecha del evento:')
num_asistentes = input ('Numero de asistentes:')

agua = 1.5
carne = 350
salsa = 0.36

total_agua = float(agua) * int(num_asistentes)
total_carne = float(carne) * int(num_asistentes)
total_salsa = float(salsa) * int(num_asistentes)

print (f"El total de agua es de:{total_agua}, de carne: {total_carne} y de salsa:{total_salsa} para un total de {num_asistentes} personas")