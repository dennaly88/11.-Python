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
print("      Ejercicio Nº  87  Eliminar Duplicados del Arreglo          ")
print("_________________________________________________________________")
 
n = int(input("¿Cuántos elementos tiene el arreglo?: "))
arreglo = []
for i in range(n):
    valor = int(input(f"  Elemento [{i}]: "))
    arreglo.append(valor)
 
sin_duplicados = []
for elemento in arreglo:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)
 
print(f"\n  Arreglo original       : {arreglo}")
print(f"  Sin duplicados         : {sin_duplicados}")
print(f"  Elementos eliminados   : {len(arreglo) - len(sin_duplicados)}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")