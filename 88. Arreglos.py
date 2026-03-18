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
print("      Ejercicio Nº  88  Contar Pares e Impares en Arreglo        ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = int(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
pares   = []
impares = []
for num in arreglo:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
 
print(f"\n  Arreglo completo : {arreglo}")
print(f"  Números pares    : {pares}  → Total: {len(pares)}")
print(f"  Números impares  : {impares}  → Total: {len(impares)}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")