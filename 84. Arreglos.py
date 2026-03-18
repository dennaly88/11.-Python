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
print("     Ejercicio Nº 84 Buscar un Elemento en el Arreglo            ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = int(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
buscar = int(input("\n  ¿Qué número desea buscar?: "))
encontrado = False
for i in range(len(arreglo)):
    if arreglo[i] == buscar:
        print(f"  ✓ Elemento {buscar} encontrado en la posición [{i}]")
        encontrado = True
 
if not encontrado:
    print(f"  ✗ El elemento {buscar} NO está en el arreglo")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")