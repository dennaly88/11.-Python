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
print("Ejercicio Nº  146: CRUD UPDATE: Actualizar Precio y Stock        ")     
print("_________________________________________________________________")



from conexion import get_conexion

def actualizar_producto(id_prod, nuevo_precio, nuevo_stock):
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        UPDATE productos
        SET precio = ?, stock = ?
        WHERE id = ? AND activo = 1
    """, (nuevo_precio, nuevo_stock, id_prod))
    afectados = cur.rowcount
    con.commit()
    con.close()
    return afectados

# ── Programa principal ──
id_upd    = int(input("ID del producto a actualizar: "))
nuevo_precio = float(input("Nuevo precio (Bs.): "))
nuevo_stock  = int(input("Nuevo stock: "))

filas = actualizar_producto(id_upd, nuevo_precio, nuevo_stock)
if filas:
    print(f"Producto ID {id_upd} actualizado correctamente.")
else:
    print("No se encontró el producto o está inactivo.")




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")