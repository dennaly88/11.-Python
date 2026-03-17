print("___________________________________________________")
print("___________________________________________________")
print("  DANNY JOSE JIMENEZ GUTIERREZ                     ")
print("  TELEFONO :0424-281-44-55                         ")
print("  CORREO : [DENNALY88@GMAIL.COM]                    ")
print("  INGENIERO EN INFORMÁTICA                         ")
print("___________________________________________________")
print("___________________________________________________")
print("\n")

print("_________________________________________________________________")
print("     Ejercicio Nº  46 Nivel de Acceso al Sistema                 ")
print("_________________________________________________________________")

nivel = int(input("Nivel de usuario (1-4): "))

accesos = {
    1: "USUARIO BÁSICO",
    2: "USUARIO AVANZADO",
    3: "SUPERVISOR",
    4: "ADMINISTRADOR"
}

resultado = accesos.get(nivel, "NIVEL NO AUTORIZADO")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
