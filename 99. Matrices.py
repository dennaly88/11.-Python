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
print("Ejercicio Nº  99  Buscar Elemento en la Matriz                   ")
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

buscar     = int(input("\n  ¿Qué elemento desea buscar?: "))
encontrado = False

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == buscar:
            print(f"  ✓ Elemento {buscar} encontrado en posición [{i}][{j}]")
            encontrado = True

if not encontrado:
    print(f"  ✗ El elemento {buscar} NO se encuentra en la matriz")
print("\n")

 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")