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
print("        Ejercicio Nº 79 Contador de Palabras Ingresadas          ")
print("_________________________________________________________________")
 
palabras = []
print("  Ingrese palabras una por una (escriba 'FIN' para terminar)\n")
 
while True:
    palabra = input("  Palabra: ").strip()
    if palabra.upper() == "FIN":
        break
    if palabra:
        palabras.append(palabra.lower())
        print(f"  ✓ Palabra '{palabra}' agregada")
 
print(f"\n  Total de palabras ingresadas : {len(palabras)}")
print(f"  Palabras únicas              : {len(set(palabras))}")
print(f"  Lista: {', '.join(palabras)}")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")