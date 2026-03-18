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
print("      Ejercicio Nº  110  Función Calculadora                    ")
print("_________________________________________________________________")

 

def calculadora(operacion, **kwargs):
    a = kwargs.get("a", 0)
    b = kwargs.get("b", 0)
    if operacion == "suma":    return a + b
    if operacion == "resta":   return a - b
    if operacion == "mult":    return a * b
    if operacion == "div":     return a / b if b != 0 else "Error"
    return "Operación no válida"

a = float(input("Valor a: "))
b = float(input("Valor b: "))
op = input("Operación (suma/resta/mult/div): ")
print(f"Resultado: {calculadora(op, a=a, b=b)}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")