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
print("Ejercicio Nº  135: SQL  Actualizar Registro por ID               ")     
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

id_upd     = int(input("ID a actualizar: "))
nuevo_nom  = input("Nuevo nombre: ")
nueva_edad = int(input("Nueva edad: "))
nuevo_cor  = input("Nuevo correo: ")

cur.execute("""
    UPDATE personas
    SET nombre = ?, edad = ?, correo = ?
    WHERE id = ?
""", (nuevo_nom, nueva_edad, nuevo_cor, id_upd))

con.commit()
if cur.rowcount:
    print(f"Registro ID {id_upd} actualizado correctamente.")
else:
    print("No se encontró el ID especificado.")
con.close()




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")