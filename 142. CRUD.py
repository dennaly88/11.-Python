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
print("            Ejercicio Nº  142: CRUD Crear Tabla Productos        ")     
print("_________________________________________________________________")


from conexion import get_conexion

def crear_tabla():
    con = get_conexion()
    cur = con.cursor()
    cur.execute("""
        IF NOT EXISTS (
            SELECT * FROM sysobjects WHERE name='productos'
        )
        CREATE TABLE productos (
            id          INT IDENTITY(1,1) PRIMARY KEY,
            nombre      NVARCHAR(150) NOT NULL,
            precio      DECIMAL(10,2) NOT NULL,
            stock       INT           DEFAULT 0,
            categoria   NVARCHAR(80),
            activo      BIT           DEFAULT 1,
            fecha_reg   DATETIME      DEFAULT GETDATE()
        )
    """)
    con.commit()
    print("Tabla 'productos' lista en SQL Server.")
    con.close()

crear_tabla()



print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")