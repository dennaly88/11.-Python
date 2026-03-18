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
print("   Ejercicio Nº  134: SQL Consultar Todos los Registros          ")     
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

cur.execute("SELECT id, nombre, edad, correo FROM personas ORDER BY id")
filas = cur.fetchall()

print(f"\n{'ID':<5} {'NOMBRE':<25} {'EDAD':<6} {'CORREO'}")
print("-" * 65)
for f in filas:
    print(f"{f.id:<5} {f.nombre:<25} {f.edad:<6} {f.correo}")

print(f"\nTotal: {len(filas)} registros.")
con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")