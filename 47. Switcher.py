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
print("               Ejercicio Nº 47 Turno Laboral                     ")
print("_________________________________________________________________")

turno = int(input("Turno (1-3): "))

turnos = {
    1: "MAÑANA (6am-2pm)",
    2: "TARDE (2pm-10pm)",
    3: "NOCHE (10pm-6am)"
}

resultado = turnos.get(turno, "TURNO INVÁLIDO")
print(resultado)
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")
