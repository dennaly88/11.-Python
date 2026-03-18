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
print("   Ejercicio Nº 90  Estadísticas Completas del Arreglo           ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = float(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
suma    = sum(arreglo)
promedio= suma / len(arreglo)
mayor   = arreglo[0]
menor   = arreglo[0]
positivos = 0
negativos = 0
 
for num in arreglo:
    if num > mayor: mayor = num
    if num < menor: menor = num
    if num >= 0: positivos += 1
    else: negativos += 1
 
print(f"\n  ===== ESTADÍSTICAS DEL ARREGLO =====")
print(f"  Arreglo        : {arreglo}")
print(f"  Total elementos: {len(arreglo)}")
print(f"  Suma           : {suma:.2f}")
print(f"  Promedio       : {promedio:.2f}")
print(f"  Mayor          : {mayor}")
print(f"  Menor          : {menor}")
print(f"  Positivos      : {positivos}")
print(f"  Negativos      : {negativos}")
print("\n")
 

 

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")