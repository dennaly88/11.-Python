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
print("        Ejercicio Nº 86 Invertir un Arreglo                      ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = int(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
invertido = []
for i in range(len(arreglo) - 1, -1, -1):
    invertido.append(arreglo[i])
 
print(f"\n  Arreglo original  : {arreglo}")
print(f"  Arreglo invertido : {invertido}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")