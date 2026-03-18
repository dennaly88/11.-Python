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
print("    Ejercicio Nº 73 Validar Cédula de Identidad                  ")
print("_________________________________________________________________")
 
while True:
    cedula = input("  Ingrese su cédula (solo números, mín 7 dígitos): ")
    if cedula.isdigit() and len(cedula) >= 7:
        print(f"  ✓ Cédula válida: {cedula}")
        break
    else:
        print("  ✗ Cédula inválida. Solo números y mínimo 7 dígitos.")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")