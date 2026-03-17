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
print("      Ejercicio Nº 62 Adivina el Número Secreto                  ")
print("_________________________________________________________________")
 
secreto = 88
intento = 0
intentos = 0
print("  Adivina el número secreto entre 1 y 100")
while intento != secreto:
    intento = int(input("  Tu intento: "))
    intentos += 1
    if intento < secreto:
        print("  → Muy bajo, intenta más alto")
    elif intento > secreto:
        print("  → Muy alto, intenta más bajo")
print(f"\n  ✓ ¡Correcto! Lo lograste en {intentos} intento(s)")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")