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
print("      Ejercicio Nº 64 Validación de Contraseña                   ")
print("_________________________________________________________________")
 
clave_correcta = "Danny16029567*"
intentos_max = 3
intentos = 0
acceso = False
print("  Sistema de acceso seguro")
while intentos < intentos_max:
    clave = input(f"  Intento {intentos + 1} — Ingrese la contraseña: ")
    intentos += 1
    if clave == clave_correcta:
        acceso = True
        break
    else:
        restantes = intentos_max - intentos
        print(f"  ✗ Contraseña incorrecta. Intentos restantes: {restantes}")
 
if acceso:
    print("  ✓ ACCESO CONCEDIDO")
else:
    print("  ✗ ACCESO BLOQUEADO — Demasiados intentos fallidos")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")