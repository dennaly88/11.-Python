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
print("Ejercicio Nº  136: SQL Eliminar Registro con Confirmación        ")     
print("_________________________________________________________________")



import pyodbc

cadena = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=CursoPython;"
    "Trusted_Connection=yes;"
)
con = pyodbc.connect(cadena)
cur = con.cursor()

id_del = int(input("ID a eliminar: "))

cur.execute("SELECT nombre FROM personas WHERE id = ?", id_del)
fila = cur.fetchone()

if fila:
    ok = input(f"¿Eliminar a '{fila.nombre}'? (s/n): ")
    if ok.lower() == 's':
        cur.execute("DELETE FROM personas WHERE id = ?", id_del)
        con.commit()
        print("Registro eliminado correctamente.")
    else:
        print("Operación cancelada.")
else:
    print("ID no encontrado.")
con.close()





print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")