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
print("       Ejercicio Nº  147: CRUD  DELETE: Baja Lógica (activo=0)   ")     
print("_________________________________________________________________")



from conexion import get_conexion

def baja_logica(id_prod):
    """Desactiva el producto sin eliminar el registro."""
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        UPDATE productos SET activo = 0
        WHERE id = ? AND activo = 1
    """, id_prod)
    afectados = cur.rowcount
    con.commit()
    con.close()
    return afectados

def baja_fisica(id_prod):
    """Elimina el registro permanentemente."""
    con = get_conexion()
    cur = con.cursor()
    cur.execute("DELETE FROM productos WHERE id = ?", id_prod)
    afectados = cur.rowcount
    con.commit()
    con.close()
    return afectados

# ── Programa principal ──
id_del = int(input("ID a dar de baja: "))
tipo   = input("Tipo: (L)ógica / (F)ísica: ").upper()

if tipo == "L":
    r = baja_logica(id_del)
    print("Baja lógica aplicada." if r else "No encontrado.")
elif tipo == "F":
    r = baja_fisica(id_del)
    print("Registro eliminado." if r else "No encontrado.")




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")