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
print("         Ejercicio Nº  50 Tipo de Soporte Técnico                ")
print("_________________________________________________________________")

nivel = int(input("Nivel de soporte (1-4): "))

soportes = {
    1: "SOPORTE BÁSICO (Chat)",
    2: "SOPORTE TÉCNICO (Teléfono)",
    3: "SOPORTE PREMIUM (Remoto)",
    4: "SOPORTE VIP (En sitio)"
}

resultado = soportes.get(nivel, "NIVEL NO DISPONIBLE")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
