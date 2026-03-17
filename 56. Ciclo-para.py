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
print("       Ejercicio Nº 56 Lista de Compras con Precio Total         ")
print("_________________________________________________________________")
 
cantidad = int(input("¿Cuántos productos desea ingresar?: "))
total = 0

for i in range(1, cantidad + 1):
    precio = float(input(f"  Precio del producto {i}: "))
    total += precio

print(f"\n  TOTAL A PAGAR: ${total:.2f}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")