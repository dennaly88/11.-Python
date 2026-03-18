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
print("Ejercicio Nº  137: SQL Búsqueda con Filtro y Parámetros         ")     
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

criterio  = input("Buscar por nombre (parcial): ")
edad_min  = int(input("Edad mínima (0 = sin filtro): "))

query = """
    SELECT id, nombre, edad, correo
    FROM personas
    WHERE nombre LIKE ?
      AND edad >= ?
    ORDER BY nombre
"""
cur.execute(query, (f"%{criterio}%", edad_min))
resultados = cur.fetchall()

if resultados:
    for f in resultados:
        print(f"  [{f.id}] {f.nombre} | {f.edad} años | {f.correo}")
else:
    print("Sin resultados.")
con.close()


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")