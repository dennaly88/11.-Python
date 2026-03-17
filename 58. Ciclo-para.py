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
print("     Ejercicio Nº 58 Promedio de Notas de un Estudiante         ")
print("_________________________________________________________________")
 
materias = int(input("¿Cuántas materias desea promediar?: "))
suma_notas = 0
for i in range(1, materias + 1):
    nota = float(input(f"  Nota de la materia {i}: "))
    suma_notas += nota
promedio = suma_notas / materias
estado = "APROBADO ✓" if promedio >= 10 else "REPROBADO ✗"


print(f"\n  Promedio: {promedio:.2f} → {estado}")
print("\n")
print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")