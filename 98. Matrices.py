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
print("Ejercicio Nº  98  Contar Positivos, Negativos y Ceros            ")
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

positivos = 0
negativos = 0
ceros     = 0

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > 0:
            positivos += 1
        elif matriz[i][j] < 0:
            negativos += 1
        else:
            ceros += 1

print("\n  === MATRIZ ===")
for fila in matriz:
    print(" ", fila)
print(f"\n  Positivos : {positivos}")
print(f"  Negativos : {negativos}")
print(f"  Ceros     : {ceros}")
print("\n")
 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")