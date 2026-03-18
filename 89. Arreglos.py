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
print("         Ejercicio Nº  89  Fusionar Dos Arreglos                 ")
print("_________________________________________________________________")
 
n1 = int(input("¿Cuántos elementos tiene el ARREGLO 1?: "))
arreglo1 = []
for i in range(n1):
    valor = int(input(f"  Arreglo1[{i}]: "))
    arreglo1.append(valor)
 
n2 = int(input("¿Cuántos elementos tiene el ARREGLO 2?: "))
arreglo2 = []
for i in range(n2):
    valor = int(input(f"  Arreglo2[{i}]: "))
    arreglo2.append(valor)
 
fusionado = arreglo1 + arreglo2
 
print(f"\n  Arreglo 1   : {arreglo1}")
print(f"  Arreglo 2   : {arreglo2}")
print(f"  Fusionado   : {fusionado}")
print(f"  Total elem. : {len(fusionado)}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")