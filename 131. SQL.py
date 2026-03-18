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
print("Ejercicio Nº  131: SQL  Conectar Python a SQL Server con pyodbc   ")     
print("_________________________________________________________________")



import pyodbc


SERVER   = input("Servidor (ej: localhost\SQLEXPRESS): ")
DATABASE = input("Base de datos: ")

cadena = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"   
)

try:
    conexion = pyodbc.connect(cadena)
    print("Conexión exitosa a SQL Server!")
    print(f"Driver: {conexion.getinfo(pyodbc.SQL_DRIVER_NAME)}")
    conexion.close()
except pyodbc.Error as e:
    print(f"Error de conexión: {e}")




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")