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
print("Ejercicio Nº  93 Mayor y Menor Elemento de la Matriz             ")
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

mayor = matriz[0][0]
menor = matriz[0][0]
pos_mayor = (0, 0)
pos_menor = (0, 0)

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            pos_mayor = (i, j)
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

print("\n  === MATRIZ ===")
for fila in matriz:
    print(" ", fila)
print(f"\n  Mayor: {mayor}  en posición {pos_mayor}")
print(f"  Menor: {menor}  en posición {pos_menor}")
print("\n")





 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")