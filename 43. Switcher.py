print("___________________________________________________")
print("___________________________________________________")
print("  DANNY JOSE JIMENEZ GUTIERREZ                     ")
print("  TELEFONO :0424-281-44-55                         ")
print("  CORREO : [DENNALY88@GMAIL.COM]                    ")
print("  INGENIERO EN INFORMÁTICA                         ")
print("___________________________________________________")
print("___________________________________________________")
print("\n")

print("_________________________________________________________________")
print("Ejercicio Nº  43      Categoría de Hotel                         ")
print("_________________________________________________________________")

estrellas = int(input("Estrellas (1-5): "))

hoteles = {
    1: "HOSTAL",
    2: "HOTEL 2★",
    3: "HOTEL 3★", 
    4: "HOTEL 4★",
    5: "HOTEL 5★ Lujo"
}

resultado = hoteles.get(estrellas, "CANTIDAD INVÁLIDA")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
