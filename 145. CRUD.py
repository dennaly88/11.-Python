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
print("Ejercicio Nº  145: CRUD READ: Buscar Producto por ID             ")     
print("_________________________________________________________________")


from conexion import get_conexion

def buscar_por_id(id_prod):
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        SELECT id, nombre, precio, stock, categoria, fecha_reg
        FROM productos WHERE id = ?
    """, id_prod)
    fila = cur.fetchone()
    con.close()
    return fila

# ── Programa principal ──
id_buscar = int(input("ID del producto a buscar: "))
p = buscar_por_id(id_buscar)

if p:
    print(f"\n{'='*40}")
    print(f"  ID        : {p.id}")
    print(f"  Nombre    : {p.nombre}")
    print(f"  Precio    : Bs. {p.precio:.2f}")
    print(f"  Stock     : {p.stock} unidades")
    print(f"  Categoría : {p.categoria}")
    print(f"  Registro  : {p.fecha_reg}")
    print(f"{'='*40}")
else:
    print("Producto no encontrado.")



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")