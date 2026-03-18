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
print("Ejercicio Nº  133: SQL Insertar Registro en SQL Server          ")     
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

nombre = input("Nombre: ")
edad   = int(input("Edad: "))
correo = input("Correo: ")

cur.execute(
    "INSERT INTO personas (nombre, edad, correo) VALUES (?, ?, ?)",
    (nombre, edad, correo)
)

# Obtener el ID generado
cur.execute("SELECT @@IDENTITY")
nuevo_id = int(cur.fetchone()[0])

con.commit()
print(f"Registro insertado con ID: {nuevo_id}")
con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")