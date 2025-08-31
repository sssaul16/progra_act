coordenad_1 = input("Introduce la coordenada x1: ")
coordenad_2 = input("Introduce la coordenada y1: ")
coordenad_3 = input("Introduce la coordenada x2: ")
coordenad_4 = input("Introduce la coordenada y2: ")

pendiente = (float(coordenad_4) - float(coordenad_2)) / (float(coordenad_3) - float(coordenad_1))
ecuacion = f"y - {coordenad_2} = {pendiente}(x - {coordenad_1})"

print(f"La pendiente de la recta es {pendiente} y la ecuación de la recta es: {ecuacion}")