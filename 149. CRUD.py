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
print("Ejercicio Nº  149: CRUD Transacciones con try/except   ")     
print("_________________________________________________________________")


from conexion import get_conexion
import pyodbc

def transferir_stock(id_origen, id_destino, cantidad):
    """
    Transfiere stock entre dos productos de forma atómica.
    Si falla algún paso, hace ROLLBACK completo.
    """
    con = get_conexion()
    try:
        cur = con.cursor()

        # Verificar stock disponible
        cur.execute("SELECT stock FROM productos WHERE id=?", id_origen)
        fila = cur.fetchone()
        if not fila or fila.stock < cantidad:
            raise ValueError("Stock insuficiente en el origen.")

        # Restar del origen
        cur.execute(
            "UPDATE productos SET stock = stock - ? WHERE id = ?",
            (cantidad, id_origen)
        )
        # Sumar al destino
        cur.execute(
            "UPDATE productos SET stock = stock + ? WHERE id = ?",
            (cantidad, id_destino)
        )

        con.commit()
        print(f"Transferencia de {cantidad} unidades completada.")

    except (pyodbc.Error, ValueError) as e:
        con.rollback()
        print(f"Error - Transacción revertida: {e}")
    finally:
        con.close()

# ── Programa principal ──
origen  = int(input("ID producto origen: "))
destino = int(input("ID producto destino: "))
cant    = int(input("Cantidad a transferir: "))
transferir_stock(origen, destino, cant)



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")