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
print("        Ejercicio Nº  109 Función Lambda y Map                   ")
print("_________________________________________________________________")



cuadrado = lambda x: x ** 2

n = int(input("Cuántos números: "))
numeros = [int(input(f"Número {i+1}: ")) for i in range(n)]

cuadrados = list(map(cuadrado, numeros))
print(f"Originales:  {numeros}")
print(f"Cuadrados:   {cuadrados}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")