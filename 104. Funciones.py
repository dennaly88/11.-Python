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
print("          Ejercicio Nº  104  Función Conversión Temperatura      ")
print("_________________________________________________________________")



def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

c = float(input("Ingrese temperatura en Celsius: "))
print(f"{c}°C = {celsius_a_fahrenheit(c):.2f}°F")
f = float(input("Ingrese temperatura en Fahrenheit: "))
print(f"{f}°F = {fahrenheit_a_celsius(f):.2f}°C")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")