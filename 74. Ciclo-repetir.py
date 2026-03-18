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
print("    Ejercicio Nº 74 Menú de Conversión de Temperatura            ")
print("_________________________________________________________________")
 
while True:
    print("\n  === CONVERSIÓN DE TEMPERATURA ===")
    print("  1. Celsius a Fahrenheit")
    print("  2. Fahrenheit a Celsius")
    print("  3. Celsius a Kelvin")
    print("  4. Salir")
    opcion = int(input("  Seleccione opción: "))
 
    if opcion == 1:
        c = float(input("  Ingrese temperatura en Celsius: "))
        print(f"  Resultado: {c:.2f} °C = {(c * 9/5) + 32:.2f} °F")
    elif opcion == 2:
        f = float(input("  Ingrese temperatura en Fahrenheit: "))
        print(f"  Resultado: {f:.2f} °F = {(f - 32) * 5/9:.2f} °C")
    elif opcion == 3:
        c = float(input("  Ingrese temperatura en Celsius: "))
        print(f"  Resultado: {c:.2f} °C = {c + 273.15:.2f} K")
    elif opcion == 4:
        print("  Saliendo del conversor...")
        break
    else:
        print("  ✗ Opción no válida")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")