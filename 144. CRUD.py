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
print("    Ejercicio Nº  144: CRUD  READ: Listar Productos              ")     
print("_________________________________________________________________")


from conexion import get_conexion

def listar_productos():
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        SELECT id, nombre, precio, stock, categoria
        FROM productos
        WHERE activo = 1
        ORDER BY categoria, nombre
    """)
    filas = cur.fetchall()
    con.close()
    return filas

# ── Programa principal ──
productos = listar_productos()

print(f"\n{'ID':<5} {'NOMBRE':<25} {'PRECIO':>10} {'STOCK':>6} {'CATEGORÍA'}")
print("=" * 65)
for p in productos:
    print(f"{p.id:<5} {p.nombre:<25} {p.precio:>10.2f} {p.stock:>6} {p.categoria}")
print(f"\nTotal productos: {len(productos)}")



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")