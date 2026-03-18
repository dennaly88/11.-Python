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
print("Ejercicio Nº  100     Tabla de Multiplicar en Formato Matriz     ")
print("_________________________________________________________________")

n = int(input("Ingrese el tamaño de la tabla (ej: 5 genera tabla 5x5): "))

matriz = []
for i in range(1, n + 1):
    fila = []
    for j in range(1, n + 1):
        fila.append(i * j)
    matriz.append(fila)

print(f"\n  === TABLA DE MULTIPLICAR {n}x{n} ===\n")
print("      ", end="")
for j in range(1, n + 1):
    print(f"{j:5}", end="")
print()
print("  " + "-" * (5 * n + 4))

for i in range(n):
    print(f"  {i + 1:2} |", end="")
    for j in range(n):
        print(f"{matriz[i][j]:5}", end="")
    print()
print("\n")




 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")