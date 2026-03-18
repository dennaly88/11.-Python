print("___________________________________________________")
print("___________________________________________________")
print("  DANNY JOSE JIMENEZ GUTIERREZ                     ")
print("  TELEFONO :0424-281-44-55                         ")
print("  CORREO : [DENNALY88@GMAIL.COM]                   ")
print("  INGENIERO EN INFORMÁTICA                         ")
print("___________________________________________________")
print("___________________________________________________")
print("\n")

print("___________________________________________________________________")
print("Ejercicio Nº  132: SQL  Crear Base de Datos y Tabla en SQL Server  ")     
print("___________________________________________________________________")


import pyodbc

cadena = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\SQLEXPRESS;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)
con = pyodbc.connect(cadena, autocommit=True)
cur = con.cursor()

# Crear base de datos si no existe
cur.execute("""
    IF NOT EXISTS (
        SELECT name FROM sys.databases WHERE name = 'CursoPython'
    )
    CREATE DATABASE CursoPython
""")
print("Base de datos CursoPython creada.")

# Cambiar a la nueva base de datos
cur.execute("USE CursoPython")

cur.execute("""
    IF NOT EXISTS (
        SELECT * FROM sysobjects WHERE name='personas'
    )
    CREATE TABLE personas (
        id      INT IDENTITY(1,1) PRIMARY KEY,
        nombre  NVARCHAR(100) NOT NULL,
        edad    INT,
        correo  NVARCHAR(150)
    )
""")
print("Tabla 'personas' creada exitosamente.")
con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")