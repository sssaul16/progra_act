cap_inicial = input("Introduce el capital inicial: ")
tasa_interes = input("Introduce la tasa de interés (en decimal): ")
periodos = input("Introduce el número de periodos: ")

interes_simple = float(cap_inicial) * (1 + float(tasa_interes)/100) * float(periodos)
interes_compuesto = float(cap_inicial) * (1 + float(tasa_interes)) ** float(periodos)

print(f"El interes simple es:{interes_simple} y el interes conpuesto es:{interes_compuesto}")

