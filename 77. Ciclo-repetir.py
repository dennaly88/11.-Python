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
print("      Ejercicio Nº 77 Registro de Empleados                      ")
print("_________________________________________________________________")
 
empleados = []
print("  Registro de empleados de la empresa\n")
 
while True:
    nombre = input("  Nombre del empleado: ")
    salario = float(input(f"  Salario de {nombre}: $"))
    empleados.append({"nombre": nombre, "salario": salario})
    print(f"  ✓ Empleado '{nombre}' registrado")
 
    otro = input("  ¿Registrar otro empleado? (s/n): ")
    if otro.lower() != "s":
        break
 
print(f"\n  === REPORTE DE EMPLEADOS ===")
for i, emp in enumerate(empleados, 1):
    print(f"  {i}. {emp['nombre']:20} Salario: ${emp['salario']:.2f}")
total_nomina = sum(e["salario"] for e in empleados)
print(f"\n  NÓMINA TOTAL: ${total_nomina:.2f}")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")