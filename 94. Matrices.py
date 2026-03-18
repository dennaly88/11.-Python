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
print("Ejercicio Nº  94  Suma de Filas y Columnas                       ")
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

print("\n  === SUMA POR FILAS ===")
for i in range(filas):
    suma_fila = sum(matriz[i])
    print(f"  Fila {i}: {matriz[i]}  → Suma = {suma_fila}")

print("\n  === SUMA POR COLUMNAS ===")
for j in range(columnas):
    suma_col = 0
    for i in range(filas):
        suma_col += matriz[i][j]
    print(f"  Columna {j}: Suma = {suma_col}")
print("\n")


 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")