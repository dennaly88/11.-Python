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
print("Ejercicio Nº  148: CRUD Menú Interactivo Completo                ")     
print("_________________________________________________________________")



from conexion import get_conexion

def listar():
    con = get_conexion()
    cur = con.cursor()
    cur.execute("SELECT id,nombre,precio,stock FROM productos WHERE activo=1")
    for f in cur.fetchall():
        print(f"  {f.id:<4} {f.nombre:<22} Bs.{f.precio:>8.2f}  Stock:{f.stock}")
    con.close()

def agregar():
    n = input("Nombre: ");  p = float(input("Precio: "))
    s = int(input("Stock: ")); c = input("Categoría: ")
    con = get_conexion()
    con.execute("INSERT INTO productos(nombre,precio,stock,categoria) VALUES(?,?,?,?)",(n,p,s,c))
    con.commit(); con.close()
    print("Producto agregado.")

def editar():
    i = int(input("ID: ")); p = float(input("Nuevo precio: "))
    s = int(input("Nuevo stock: "))
    con = get_conexion()
    con.execute("UPDATE productos SET precio=?,stock=? WHERE id=?",(p,s,i))
    con.commit(); con.close()
    print("Actualizado.")

def eliminar():
    i = int(input("ID: "))
    con = get_conexion()
    con.execute("UPDATE productos SET activo=0 WHERE id=?", i)
    con.commit(); con.close()
    print("Producto desactivado.")

MENU = {"1": listar, "2": agregar, "3": editar, "4": eliminar}

while True:
    print("\n1-Listar  2-Agregar  3-Editar  4-Eliminar  0-Salir")
    op = input("Opción: ")
    if op == "0": break
    MENU.get(op, lambda: print("Opción inválida"))()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")