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
print("Ejercicio Nº  141: CRUD  Módulo de Conexión Reutilizable         ")     
print("_________________________________________________________________")


# archivo: conexion.py
# Módulo base que se importa en todos los ejercicios del CRUD
import pyodbc

SERVER   = "localhost\SQLEXPRESS"
DATABASE = "CursoPython"

def get_conexion():
    """Retorna una conexión activa a SQL Server."""
    cadena = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(cadena)

# ── Prueba de la conexión ──
if __name__ == "__main__":
    try:
        con = get_conexion()
        print(f"Conectado a: {DATABASE} en {SERVER}")
        con.close()
    except pyodbc.Error as e:
        print(f"Error: {e}")



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")