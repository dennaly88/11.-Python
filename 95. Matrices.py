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
print("Ejercicio Nº  95 Transpuesta de una Matriz                       ")
print("_________________________________________________________________")

filas    = int(input("Ingrese el número de filas   : "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

transpuesta = []
for j in range(columnas):
    fila_t = []
    for i in range(filas):
        fila_t.append(matriz[i][j])
    transpuesta.append(fila_t)

print("\n  === MATRIZ ORIGINAL ===")
for fila in matriz:
    print(" ", fila)
print("\n  === MATRIZ TRANSPUESTA ===")
for fila in transpuesta:
    print(" ", fila)
print("\n")

 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")