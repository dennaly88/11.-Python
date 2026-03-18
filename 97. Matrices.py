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
print("Ejercicio Nº  97  Sumar Dos Matrices                             ")
print("_________________________________________________________________")

filas    = int(input("Ingrese el número de filas   : "))
columnas = int(input("Ingrese el número de columnas: "))

print("\n  === INGRESE MATRIZ A ===")
matrizA = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"  A[{i}][{j}]: "))
        fila.append(valor)
    matrizA.append(fila)

print("\n  === INGRESE MATRIZ B ===")
matrizB = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"  B[{i}][{j}]: "))
        fila.append(valor)
    matrizB.append(fila)

matrizC = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(matrizA[i][j] + matrizB[i][j])
    matrizC.append(fila)

print("\n  === MATRIZ A ===")
for fila in matrizA:
    print(" ", fila)
print("\n  === MATRIZ B ===")
for fila in matrizB:
    print(" ", fila)
print("\n  === MATRIZ A + B ===")
for fila in matrizC:
    print(" ", fila)
print("\n")

 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")