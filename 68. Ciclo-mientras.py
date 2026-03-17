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
print("      Ejercicio Nº 68 Calculadora Básica con Repetición          ")
print("_________________________________________________________________")
 
continuar = "s"
while continuar.lower() == "s":
    num1 = float(input("\n  Número 1: "))
    operador = input("  Operador (+, -, *, /): ")
    num2 = float(input("  Número 2: "))
 
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/" and num2 != 0:
        resultado = num1 / num2
    else:
        print("  ✗ Operación no válida o división entre cero")
        continuar = input("  ¿Desea continuar? (s/n): ")
        continue
 
    print(f"  Resultado: {num1} {operador} {num2} = {resultado:.2f}")
    continuar = input("  ¿Desea realizar otra operación? (s/n): ")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")