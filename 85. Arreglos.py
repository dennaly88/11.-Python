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
print("     Ejercicio Nº 85 Ordenar Arreglo de Forma Ascendente         ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = int(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
print(f"\n  Arreglo original  : {arreglo}")
 
for i in range(len(arreglo)):
    for j in range(len(arreglo) - i - 1):
        if arreglo[j] > arreglo[j + 1]:
            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
 
print(f"  Arreglo ordenado  : {arreglo}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")