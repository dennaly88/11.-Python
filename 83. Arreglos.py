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
print("        Ejercicio Nº 83 Suma y Promedio del Arreglo              ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = float(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
suma = 0
for elemento in arreglo:
    suma += elemento
promedio = suma / len(arreglo)
 
print(f"\n  Arreglo  : {arreglo}")
print(f"  Suma     : {suma:.2f}")
print(f"  Promedio : {promedio:.2f}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")