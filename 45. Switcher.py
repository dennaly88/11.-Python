print("___________________________________________________")
print("___________________________________________________")
print("  DANNY JOSE JIMENEZ GUTIERREZ                     ")
print("  TELEFONO :0424-281-44-55                         ")
print("  CORREO : [DENNALY88@GMAIL.COM]                   ")
print("  INGENIERO EN INFORMÁTICA                         ")
print("___________________________________________________")
print("___________________________________________________")
print("\n")

print("_________________________________________________________________")
print("     Ejercicio Nº 45  Tipo de Vehículo por Cilindrada            ")
print("_________________________________________________________________")

cilindrada = int(input("Cilindrada (1-6): "))

vehiculos = {
    1: "MOTO PEQUEÑA",
    2: "MOTO MEDIANA",
    3: "MOTO GRANDE",
    4: "AUTOMÓVIL PEQUEÑO",
    5: "AUTOMÓVIL MEDIANO",
    6: "CAMIONETA",
    7: "CAMIÓN"
}

resultado = vehiculos.get(cilindrada, "OPCIÓN INVÁLIDA")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
