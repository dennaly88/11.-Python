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
print("     Ejercicio Nº 82 Mayor y Menor Elemento del Arreglo          ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos números desea ingresar?: "))
numeros = []
for i in range(n):
    num = int(input(f"  Número [{i}]: "))
    numeros.append(num)
 
mayor = numeros[0]
menor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
 
print(f"\n  Arreglo : {numeros}")
print(f"  Mayor   : {mayor}")
print(f"  Menor   : {menor}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")