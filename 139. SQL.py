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
print("Ejercicio Nº  139: SQL Procedimiento Almacenado desde Python    ")     
print("_________________________________________________________________")



import pyodbc

# Primero crear el SP en SQL Server Management Studio:
# CREATE PROCEDURE sp_buscar_persona
#     @nombre NVARCHAR(100)
# AS
# BEGIN
#     SELECT * FROM personas WHERE nombre LIKE '%'+@nombre+'%'
# END

cadena = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=CursoPython;"
    "Trusted_Connection=yes;"
)
con = pyodbc.connect(cadena)
cur = con.cursor()

nombre = input("Buscar persona: ")

# Ejecutar procedimiento almacenado
cur.execute("{CALL sp_buscar_persona (?)}", nombre)
filas = cur.fetchall()

for f in filas:
    print(f"  {f.id} | {f.nombre} | {f.edad} | {f.correo}")

con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")