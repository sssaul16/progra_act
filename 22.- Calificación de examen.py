total_pregun = input("Cuantas preguntas tiene el examen?")
correctas = input("Cuantas preguntas respondiste correctamente?")
nota = (int(correctas) * 10) / int(total_pregun)
print(f"Tu nota es: {nota}") 