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
print("            Ejercicio Nº  48 Tipo de Batería                     ")
print("_________________________________________________________________")

tipo = int(input("Tipo de batería (1-4): "))

baterias = {
    1: "ALKALINA",
    2: "NI-MH RECARGABLE",
    3: "LITIO",
    4: "LITIO POLÍMERO"
}

resultado = baterias.get(tipo, "TIPO NO EXISTE")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
