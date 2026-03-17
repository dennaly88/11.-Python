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
print("     Ejercicio Nº 69   Acumulador de Ventas Diarias              ")
print("_________________________________________________________________")
 
dia = 1
total_ventas = 0
print("  Ingrese 0 para finalizar el registro de ventas\n")
while True:
    venta = float(input(f"  Venta del día {dia}: $"))
    if venta == 0:
        break
    total_ventas += venta
    print(f"  ✓ Venta registrada | Acumulado: ${total_ventas:.2f}")
    dia += 1
 
print(f"\n  TOTAL DE VENTAS: ${total_ventas:.2f} en {dia - 1} día(s)")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")