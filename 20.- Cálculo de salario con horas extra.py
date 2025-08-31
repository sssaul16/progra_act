hora_extra = int(input ('Cuantas horas extra trabajaste?'))
paga_h_extra = 80
paga_hora = 63
horas_normales = 40
paga_normal = paga_hora * horas_normales
dinero_extra = hora_extra * paga_h_extra 

paga_extra = dinero_extra + paga_normal

print(f"El salario total es de {paga_extra} pesos")