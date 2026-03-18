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
print("Ejercicio Nº  138: SQL Inserción Múltiple con executemany       ")     
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

registros = [
    ("Pedro Pérez",   28, "pedro@mail.com"),
    ("Luisa Gómez",   35, "luisa@mail.com"),
    ("Ramón Torres",  22, "ramon@mail.com"),
    ("Carla Méndez",  41, "carla@mail.com"),
    ("José Blanco",   30, "jose@mail.com"),
]

cur.fast_executemany = True   # Optimización para SQL Server
cur.executemany(
    "INSERT INTO personas (nombre, edad, correo) VALUES (?, ?, ?)",
    registros
)

con.commit()
print(f"Se insertaron {len(registros)} registros en SQL Server.")
con.close()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")