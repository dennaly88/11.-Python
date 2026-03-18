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
print("    Ejercicio Nº  143: CRUD  CREATE: Insertar Producto           ")     
print("_________________________________________________________________")



from conexion import get_conexion

def insertar_producto(nombre, precio, stock, categoria):
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO productos (nombre, precio, stock, categoria)
        VALUES (?, ?, ?, ?)
    """, (nombre, precio, stock, categoria))
    cur.execute("SELECT @@IDENTITY")
    nuevo_id = int(cur.fetchone()[0])
    con.commit()
    con.close()
    return nuevo_id

# ── Programa principal ──
nombre    = input("Nombre del producto: ")
precio    = float(input("Precio (Bs.): "))
stock     = int(input("Stock inicial: "))
categoria = input("Categoría: ")

id_nuevo = insertar_producto(nombre, precio, stock, categoria)
print(f"Producto insertado con ID: {id_nuevo}")




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")