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
print("Ejercicio Nº  140: SQL  Reporte con Estadísticas SQL Server      ")     
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

cur.execute("""
    SELECT
        COUNT(*)         AS total,
        AVG(CAST(edad AS FLOAT)) AS promedio,
        MIN(edad)        AS minimo,
        MAX(edad)        AS maximo,
        (SELECT TOP 1 nombre FROM personas ORDER BY edad DESC) AS mayor
    FROM personas
""")
r = cur.fetchone()

print(f"{'='*45}")
print(f"  ESTADÍSTICAS - SQL SERVER")
print(f"{'='*45}")
print(f"  Total registros : {r.total}")
print(f"  Edad promedio   : {r.promedio:.1f} años")
print(f"  Edad mínima     : {r.minimo} años")
print(f"  Edad máxima     : {r.maximo} años")
print(f"  Persona mayor   : {r.mayor}")
print(f"{'='*45}")
con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")