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
print("Ejercicio Nº  150: CRUD  Reporte Final con Pandas y SQL Server   ")     
print("_________________________________________________________________")





import pandas as pd
from sqlalchemy import create_engine

# SQLAlchemy engine para SQL Server
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/CursoPython"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Leer tabla completa con pandas
df = pd.read_sql("SELECT * FROM productos WHERE activo=1", engine)

# Estadísticas por categoría
reporte = df.groupby("categoria").agg(
    total_productos = ("id",     "count"),
    precio_promedio = ("precio", "mean"),
    stock_total     = ("stock",  "sum"),
    precio_max      = ("precio", "max"),
).round(2)

print("\n===== REPORTE POR CATEGORÍA =====")
print(reporte.to_string())
print(f"\nTotal general: {len(df)} productos activos")
print(f"Valor inventario: Bs. {(df['precio']*df['stock']).sum():,.2f}")

# Exportar a Excel
reporte.to_excel("reporte_productos.xlsx")
print("Reporte exportado a reporte_productos.xlsx")




print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")