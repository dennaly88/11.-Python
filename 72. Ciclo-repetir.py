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
print("   Ejercicio Nº 72 Registro de Notas hasta Ingresar -1           ")
print("_________________________________________________________________")
 
notas = []
print("  Ingrese notas (escriba -1 para terminar)")
while True:
    nota = float(input("  Nota: "))
    if nota == -1:
        break
    notas.append(nota)
    print(f"  ✓ Nota registrada")
 
if notas:
    promedio = sum(notas) / len(notas)
    print(f"\n  Total de notas  : {len(notas)}")
    print(f"  Promedio        : {promedio:.2f}")
    print(f"  Nota más alta   : {max(notas)}")
    print(f"  Nota más baja   : {min(notas)}")
else:
    print("  No se registraron notas.")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")