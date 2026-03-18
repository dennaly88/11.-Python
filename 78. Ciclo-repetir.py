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
print("      Ejercicio Nº 78 Validar Rango de Edad                      ")
print("_________________________________________________________________")
 
while True:
    edad = int(input("  Ingrese su edad (entre 1 y 120): "))
    if 1 <= edad <= 120:
        if edad < 13:
            categoria = "NIÑO"
        elif edad < 18:
            categoria = "ADOLESCENTE"
        elif edad < 60:
            categoria = "ADULTO"
        else:
            categoria = "ADULTO MAYOR"
        print(f"  ✓ Edad válida: {edad} años → Categoría: {categoria}")
        break
    else:
        print("  ✗ Edad fuera de rango. Debe estar entre 1 y 120.")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")