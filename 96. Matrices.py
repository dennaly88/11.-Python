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
print("Ejercicio Nº  96 Diagonal Principal de Matriz Cuadrada           ")
print("_________________________________________________________________")

n = int(input("Ingrese el tamaño de la matriz cuadrada (NxN): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"  Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

diagonal = []
suma_diagonal = 0
for i in range(n):
    diagonal.append(matriz[i][i])
    suma_diagonal += matriz[i][i]

print("\n  === MATRIZ (diagonal resaltada) ===")
for i in range(n):
    print("  ", end="")
    for j in range(n):
        if i == j:
            print(f"[{matriz[i][j]:3}]", end="")
        else:
            print(f"{matriz[i][j]:5}", end="")
    print()

print(f"\n  Diagonal principal : {diagonal}")
print(f"  Suma diagonal      : {suma_diagonal}")
print("\n")
 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")