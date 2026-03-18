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
print("    Ejercicio Nº 75 Acumulador de Productos con IVA              ")
print("_________________________________________________________________")
 
total = 0
cantidad_productos = 0
IVA = 0.16
print("  Ingrese precios de productos (0 para terminar)\n")
 
while True:
    precio = float(input(f"  Precio del producto {cantidad_productos + 1}: $"))
    if precio == 0:
        break
    total += precio
    cantidad_productos += 1
    print(f"  ✓ Subtotal: ${total:.2f}")
 
iva_monto = total * IVA
total_con_iva = total + iva_monto
print(f"\n  Subtotal          : ${total:.2f}")
print(f"  IVA (16%)         : ${iva_monto:.2f}")
print(f"  TOTAL CON IVA     : ${total_con_iva:.2f}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")