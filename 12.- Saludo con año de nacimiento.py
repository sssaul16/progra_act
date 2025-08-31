nombre = input("Cual es tu nombre?")
edad = input("Cual es tu edad?")

import datetime
ano = datetime.datetime.now().year
nacimiento = ano - int(edad)
print(f"Hola {nombre} tu año de nacimiento es: {nacimiento}")